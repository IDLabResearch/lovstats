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

def getDataType(ref):
    datadict = {
        "int": rdflib.XSD.integer,
        "float": rdflib.XSD.float
    }
    return datadict.get(ref, rdflib.XSD.string)

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
lovc = rdflib.Namespace("https://w3id.org/lovcube/ns/lovcube#")
lrd = rdflib.Namespace('http://example.com/lovrestrictiondata#')
prov = rdflib.Namespace('http://www.w3.org/ns/prov#')
lovstats = rdflib.Namespace('http://example.com/lovstats#')
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
        g.namespace_manager.bind('lrd', lrd)
        g.namespace_manager.bind('qb', qb)
        g.namespace_manager.bind('xsd', xsd)
        g.namespace_manager.bind('rdf', rdf)
        g.namespace_manager.bind('rdfs', rdfs)

        dataset = rdflib.BNode()
        g.add((dataset, rdflib.RDF.type, qb.DataSet))
        g.add((dataset, rdflib.RDF.type, lovc.Dataset))
        g.add((dataset, rdflib.RDF.type, prov.Entity))
        g.add((dataset, qb.structure, lrd['lovstats2018datastructure']))

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

        # link dataset to generation activity
        g.add((provGenerationActivity, rdflib.RDF.type, prov.Activity))
        g.add((dataset, prov.qualifiedGeneration, provGeneration))


        # Add observations
        index = 0
        for stat_name,stat_dict in rdf_stats.get_stats_results().iteritems():
            for detectors_name,detectors_dict in stat_dict.get('detectors', {}).iteritems():
                for results_name,results_dict in detectors_dict.get('results', {}).iteritems():
                    observ = rdflib.BNode()
                    g.add((observ, rdflib.RDF.type, qb.Observation))
                    g.add((observ, rdflib.RDF.type, prov.Entity))
                    g.add((observ, rdflib.RDF.type, lovc.RestrictionTypeStatistic))
                    g.add((observ, qb.dataSet, dataset))
                    g.add((observ, lrd['executionTimeDimension'], rdflib.Literal(executionTime)))
                    g.add((observ, lrd['ontologyVersionDimension'], rdflib.Literal("")))
                    g.add((observ, lrd['restrictionTypeDimension'], lrd[detectors_name]))
                    g.add((observ, lrd['implementationDimension'], lrd[detectors_dict.get('implementation', '')]))
                    g.add((observ, lrd['detectorVersionDimension'], lrd[detectors_dict.get('version', '')]))
                    g.add((observ, lrd[results_name], rdflib.Literal(results_dict.get('value', ''), datatype=getDataType(results_dict.get('type', 'string')))))

                    # link observations to generation activity
                    g.add((observ, prov.qualifiedGeneration, provGeneration))



                    #    print("\t%s" % stat_name)
        #    for subname, result in stat_dict.iteritems():
        #        if type(result) == dict or type(result) == list:
        #            if subname in ('usage_count'):
        #                print("\t\t%s:" % subname)
        #                for subsubname, subresult in result.iteritems():
        #                    #if subresult > 0:
        #                    print("\t\t\t%s: %s" % (subsubname, subresult))
        #            else:
        #                print("\t\tlen(%s): %d" % (subname, len(result)))
        #        else:
        #            print("\t\t%s: %s" % (subname, result))
            index += 1
        print g.serialize(format='turtle')
       
