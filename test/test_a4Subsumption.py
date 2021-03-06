import unittest

import sys
import helpers
sys.path.append('../LODStats')
sys.path.append('../src/restriction-types-stats')
sys.path.append('../src/')
from A4Subsumption import A4Subsumption
import lodstats
from lodstats import RDFStats

testfile_path = helpers.resources_path

class TestA4Subsumption(unittest.TestCase):

    def setUp(self):
        lodstats.stats.stats_to_do = []
        lodstats.stats.results = {}

 #   def test_amount_hierarchies(self):
 #       uri = 'file://' + testfile_path + 'hierarchies.nt'
 #       rdfstats = RDFStats(uri, format="nt", stats=[A4Subsumption])
 #       rdfstats.start_statistics()
 #       self.assertEqual(rdfstats.get_stats_results()['a4subsumption']['subsumptionDetectorRdfsSubClassOf'], 3)

 #   def test_amount_subclasses(self):
 #       uri = 'file://' + testfile_path + 'hierarchies.nt'
 #       rdfstats = RDFStats(uri, format="nt", stats=[A4Subsumption])
 #       rdfstats.start_statistics()
 #       self.assertEqual (rdfstats.get_stats_results()['a4subsumption']['amount_subclasses'], 8)

 #   def test_avg(self):
 #       uri = 'file://' + testfile_path + 'hierarchies.nt'
 #       rdfstats = RDFStats(uri, format="nt", stats=[A4Subsumption])
 #       rdfstats.start_statistics()
 #       self.assertEqual (rdfstats.get_stats_results()['a4subsumption']['avg_depth'], 2.0)

 #   def test_median(self):
 #       uri = 'file://' + testfile_path + 'hierarchies.nt'
 #       rdfstats = RDFStats(uri, format="nt", stats=[A4Subsumption])
 #       rdfstats.start_statistics()
 #       self.assertEqual (rdfstats.get_stats_results()['a4subsumption']['median_depth'], 2.0)

    def test_owl_subclasses(self):
        uri = 'file://' + testfile_path + 'owl_subclasses.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A4Subsumption])
        rdfstats.start_statistics()
        self.assertEqual(rdfstats.get_stats_results()['a4subsumption']['detectors']['subsumptionDetectorOwlSubClassOf']['results']['restrictionTypeOccurrence']['value'], 4)
