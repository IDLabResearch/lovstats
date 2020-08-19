#!/usr/bin/env python
"""
Original work Copyright 2013 AKSW Research Group http://aksw.org/
Modified work Copyright 2018 Ghent University - imec - IDLab, Sven Lieber

Modifications:
- Adding the possibility to dynamically load a different stats-folder

This file is part of LODStats.

LODStats is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

LODStats is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with LODStats.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
import datetime
import importlib
import ntpath
import rdflib

from optparse import OptionParser

import lodstats.RDFStats
import lodstats.config
import lodstats.stats

import logging
logger = logging.getLogger("lodstats")

from pprint import pprint
sys.path.append('/src')

parser = OptionParser(usage="usage: %prog [options] [-m model.{rdf,nt,...}] file/URI [file/URI ...]")
parser.add_option('-v', '--void', action='store_true', help='generate VoID')
parser.add_option('-c', '--count', action='store_true', help='just count triples, no statistics')
parser.add_option('-f', '--format', dest='format', help='specify RDF format', metavar="FORMAT")
parser.add_option('-p', '--progress', action='store_true', help='show progress')
parser.add_option('-a', '--all-stats', action='store_true', help='do all available statistics')
parser.add_option('-l', '--lod-stats', action='store_true', help='do statistics for lodstats')
parser.add_option('-z', '--specific-stats', dest='specific_stats', help='do specific statistics for lodstats')
parser.add_option('-i', '--intermediate-stats', action='store_true', help='print intermediate statistics every 100k triples')
parser.add_option('-m', '--rdf-model', help='parse and do stats for everything that isDefinedBy supplied model')
parser.add_option('-s', '--schema-syntax-owl', action='store_true', help='do stats for RDF-Schema, -Syntax, Owl')
parser.add_option('-d', '--debug', action='store_true', help='print debugging output')
parser.add_option('-o', '--other-stats-folder', dest='other_stats_folder', help='Use also this folder to look for stats')
parser.add_option('-u', '--ontology-uri', dest='ontology_uri', help='The URI of the provided ontology')
parser.add_option('-r', '--result-file', dest='result_file', help='The name of the file where the statistics should be stored')
parser.add_option('-b', '--ontology-repository-uri', dest='ontology_repository_uri', help='The URI of the repository this ontology was obtained from')
(options, args) = parser.parse_args()

if len(args) == 0:
    parser.print_help()
    exit(2)

lodstats.config.disable_debug()
if options.debug:
    lodstats.config.enable_debug()

stats = []
new_stats = []
other_stats = []

if options.count:
    stats = []
    new_stats = []
elif options.void:
    stats = lodstats.stats.void_stats
    new_stats = []
elif options.schema_syntax_owl:
    stats = lodstats.stats.vocab_stats
    new_stats = []
elif options.rdf_model:
    model_stats = [lodstats.stats.ParsedVocabulary, options.rdf_model]
    stats = []
    new_stats = model_stats
elif options.lod_stats:
    stats = lodstats.stats.lodstats_old
    new_stats = []
elif options.all_stats:
    stats = lodstats.stats.available_stats
    new_stats = []
elif options.specific_stats:
    specific_stats = options.specific_stats.split(',')
    stats = []
    for stat in specific_stats:
        st = eval('lodstats.stats.'+stat)
        stats.append(st)
    new_stats = []
    print stats
else:
    stats = []
    new_stats = []

if options.other_stats_folder:
    other_stats_module = importlib.import_module(options.other_stats_folder)
    other_stats = other_stats_module.all_stats

stats += other_stats
start_time = datetime.datetime.now()

######################
# Callback functions #
######################
def callback_function_download(remote_file):
    now = datetime.datetime.now()
    time_delta = (now-start_time).seconds
    if time_delta > 0:
        print("\r%d of %d KB loaded, %d KB/s." % (remote_file.bytes_downloaded/1024,
        remote_file.content_length/1024, (remote_file.bytes_downloaded/1024)/time_delta)),
        sys.stdout.flush()
    else:
        print("\r%d of %d KB loaded." % (remote_file.bytes_downloaded/1024,
        remote_file.content_length/1024)),
        sys.stdout.flush()

def callback_function_extraction(archive_extractor):
    manyspaces = ' '*72
    print("\r%s" % manyspaces),
    sys.stdout.flush()
    now = datetime.datetime.now()
    time_delta = (now-start_time).seconds
    if time_delta > 0:
        print("\rFetch done %d KB, %d KB uncomp., %d KB/s." % (archive_extractor.original_file_size/1024, archive_extractor.bytes_extracted/1024, (archive_extractor.bytes_extracted/1024)/time_delta))
        sys.stdout.flush()
    else:
        print("\rFetch done %d KB, %d KB uncomp." % (archive_extractor.original_file_size/1024, archive_extractor.bytes_extracted/1024))
        sys.stdout.flush()

def callback_function_statistics(rdf_file):
    if rdf_file.get_no_of_triples() > 0:
        now = datetime.datetime.now()
        time_delta = (now-start_time).seconds
        if time_delta > 0:
            print("\r%d triples done, %d/s, %d warnings" % (rdf_file.get_no_of_triples(),
            rdf_file.get_no_of_triples()/time_delta, rdf_file.warnings)),
        else:
            print("\r%d triples done, %d warnings" % (rdf_file.get_no_of_triples(), rdf_file.warnings)),
        sys.stdout.flush()
        if not options.count and options.intermediate_stats and rdf_file.no_of_statements % 100000 == 0:
            print("Results (from custom code):")
            for stat_name,stat_dict in rdf_file.stats_results.iteritems():
                print("\t%s" % stat_name)
                for subname, result in stat_dict.iteritems():
                    if type(result) == dict or type(result) == list:
                        print("\t\tlen(%s): %d" % (subname, len(result)))
                    else:
                        print("\t\t%s: %s" % (subname, result))


def create_dataset(measure_name, datasets, graph, provGeneration, provGenerationActivity):

    # A mapping of measure types to data structure IRIs used in lovstats.ttl
    measure_to_structure_mappings = {
        "restrictionTypeOccurrence": "restrictionTypesAmount",
        "hierarchyOccurrence": "hierarchyAmountDistribution",
        "minHierarchyDepth": "minHierarchyDepthsDistribution",
        "maxHierarchyDepth": "maxHierarchyDepthsDistribution",
        "averageHierarchyDepth": "meanHierarchyDepthsDistribution",
        "medianHierarchyDepth": "medianHierarchyDepthsDistribution"
    }

    # if already seen, return saved blank node id
    if measure_name in datasets:
        return datasets[measure_name]
    else:
        dataset = rdflib.BNode()
        graph.add((dataset, rdflib.RDF.type, qb.DataSet))
        graph.add((dataset, rdflib.RDF.type, lovc.Dataset))
        graph.add((dataset, rdflib.RDF.type, prov.Entity))
        graph.add((dataset, qb.structure, rls[measure_to_structure_mappings[measure_name]]))
        graph.add((dataset, prov.qualifiedGeneration, provGeneration))
        graph.add((dataset, prov.wasGeneratedBy, provGenerationActivity))
        datasets[measure_name] = dataset
        return dataset

####################
# Processing logic #
####################

for resource_uri in args:
    #if not os.access(resource_uri, os.R_OK):
        #print("File not found/unreadable")
        #exit(3)

    rdf_stats = lodstats.RDFStats(resource_uri, stats=stats, new_stats=new_stats, format=options.format)

    if options.progress:
        rdf_stats.set_callback_function_download(callback_function_download)
        rdf_stats.set_callback_function_extraction(callback_function_extraction)
        rdf_stats.set_callback_function_statistics(callback_function_statistics)
    else:
        rdf_stats.disable_callback_function_download()
        rdf_stats.disable_callback_function_extraction()
        rdf_stats.disable_callback_function_statistics()

    rdf_stats.start_statistics()

if options.void:
    print(rdf_stats.voidify("turtle"))
    

rdf = rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
rdfs = rdflib.Namespace('http://www.w3.org/2000/01/rdf-schema#')
skos = rdflib.Namespace('http://www.w3.org/2004/02/skos/core#')
xsd = rdflib.Namespace('http://www.w3.org/2001/XMLSchema#')
qb = rdflib.Namespace("http://purl.org/linked-data/cube#")
lovc = rdflib.Namespace("https://w3id.org/montolo/ns/montolo-voc#")
rls = rdflib.Namespace('https://w3id.org/montolo/ns/montolo#')
prov = rdflib.Namespace('http://www.w3.org/ns/prov#')
lovstats = rdflib.Namespace('https://w3id.org/lovcube/ns/relovstats#')
sdmx_attribute = rdflib.Namespace('http://purl.org/linked-data/sdmx/2009/attribute#')
sdmx_concept = rdflib.Namespace('http://purl.org/linked-data/sdmx/2009/concept#')


if not options.void:
    #print("Basic stats: %s triples, %s warnings" % (rdf_stats.get_no_of_triples(), rdf_stats.get_no_of_warnings()))
    if not options.count:
        #print("Results (from custom code):")
        #pprint(rdf_stats.get_stats_results())
        executionTime = datetime.datetime.utcnow()
        g=rdflib.Graph()
        g.namespace_manager.bind('prov', prov)
        g.namespace_manager.bind('lovc', lovc)
        g.namespace_manager.bind('rls', rls)
        g.namespace_manager.bind('qb', qb)
        g.namespace_manager.bind('xsd', xsd)
        g.namespace_manager.bind('rdf', rdf)
        g.namespace_manager.bind('rdfs', rdfs)
        g.namespace_manager.bind('sdmx-attribute', sdmx_attribute)

        # create a dictionary to hold a dataset for reach measure
        all_datasets = {}


        # Add provenance

        # prov generation activity
        provGeneration = rdflib.BNode()
        provGenerationActivity = rdflib.BNode()
        g.add((provGenerationActivity, rdflib.RDF.type, prov.Activity))

        # prov qualified generation (which defines type and related activity)
        g.add((provGeneration, rdflib.RDF.type, prov.Generation))
        g.add((provGeneration, rdflib.RDF.type, prov.InstantaneousEvent))
        g.add((provGeneration, prov.atTime, rdflib.Literal(executionTime)))
        g.add((provGeneration, prov.activity, provGenerationActivity))

        # Create a generation activity
        g.add((provGenerationActivity, rdflib.RDF.type, prov.Activity))

        # Add observations
        index = 0

        # Loop over restriction types:
        for stat_name,stat_dict in rdf_stats.get_stats_results().iteritems():
            # Loop over different detectors:
            for detectors_name,detectors_dict in stat_dict.get('detectors', {}).iteritems():
                # Loop over different results:
                for results_name,results_dict in detectors_dict.get('results', {}).iteritems():
                    observ = rdflib.BNode()

                    # Create a dataset for each measure (the function returns the blank node id if the dataset was already created)
                    dataset = create_dataset(results_name, all_datasets, g, provGeneration, provGenerationActivity)

                    # Create the observation
                    g.add((observ, rdflib.RDF.type, qb.Observation))
                    g.add((observ, rdflib.RDF.type, prov.Entity))
                    g.add((observ, rdflib.RDF.type, lovc.RestrictionTypeStatistic))
                    g.add((observ, qb.dataSet, dataset))
                    g.add((observ, rls['executionTimeDimension'], rdflib.Literal(executionTime)))
                    g.add((observ, rls['restrictionTypeDimension'], rls[detectors_dict.get('restriction-type')]))
                    g.add((observ, rls['detectorDimension'], rls[detectors_name]))
                    g.add((observ, rls['detectorVersionDimension'], rls[detectors_dict.get('version', '')]))
                    g.add((observ, rls['ontologyRepositoryDimension'], rdflib.URIRef(options.ontology_repository_uri)))
                    g.add((observ, rls[results_name], rdflib.Literal(results_dict.get('value', ''), datatype=results_dict.get('type', 'string'))))

                    if options.ontology_uri:
                        g.add((observ, rls['ontologyVersionDimension'], rdflib.URIRef(options.ontology_uri)))
                    else:
                        g.add((observ, rls['ontologyVersionDimension'], rdflib.Literal("")))
                    # link observations to generation activity
                    g.add((observ, prov.qualifiedGeneration, provGeneration))

            index += 1

        f = open(options.result_file, "w")
        f.write(g.serialize(format='turtle'))
        exit(0)

