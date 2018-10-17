import unittest

import sys
import helpers
sys.path.append('../LODStats')
sys.path.append('../constraint-type-stats')
from C1Subsumption import C1Subsumption
from lodstats.stats.StringLength import StringLength
from lodstats.stats.SubclassUsage import SubclassUsage
import lodstats
from lodstats import RDFStats
from pprint import pprint

testfile_path = helpers.resources_path

class TestC1Subsumption(unittest.TestCase):

    def setUp(self):
        lodstats.stats.stats_to_do = []
        lodstats.stats.results = {}

    def test_all(self):
        uri = 'file://' + testfile_path + 'hierarchies.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[C1Subsumption])
        rdfstats.start_statistics()
        assert(rdfstats.get_stats_results()['c1subsumption']['amount_hierarchies'] == 3)
        assert (rdfstats.get_stats_results()['c1subsumption']['amount_subclasses'] == 8)
        assert (rdfstats.get_stats_results()['c1subsumption']['avg_depth'] == 2.0)
        assert (rdfstats.get_stats_results()['c1subsumption']['median_depth'] == 2.0)