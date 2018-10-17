import unittest

import sys
import helpers
sys.path.append('../LODStats')
sys.path.append('../constraint-type-stats')
from A69DisjointProperties import A69DisjointProperties
import lodstats
from lodstats import RDFStats

testfile_path = helpers.resources_path

class TestA69DisjointProperties(unittest.TestCase):

    def setUp(self):
        lodstats.stats.stats_to_do = []
        lodstats.stats.results = {}

    def test_amount(self):
        uri = 'file://' + testfile_path + 'disjointProperties.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A69DisjointProperties])
        rdfstats.start_statistics()
        self.assertEqual(rdfstats.get_stats_results()['a69disjointproperties']['amount_disjoint_properties'], 11)

    def test_avg(self):
        uri = 'file://' + testfile_path + 'disjointProperties.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A69DisjointProperties])
        rdfstats.start_statistics()
        self.assertEqual (rdfstats.get_stats_results()['a69disjointproperties']['avg_disjoint'], 2.75)

    def test_median(self):
        uri = 'file://' + testfile_path + 'disjointProperties.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A69DisjointProperties])
        rdfstats.start_statistics()
        self.assertEqual (rdfstats.get_stats_results()['a69disjointproperties']['median_disjoint'], 2.5)

    def test_min(self):
        uri = 'file://' + testfile_path + 'disjointProperties.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A69DisjointProperties])
        rdfstats.start_statistics()
        self.assertEqual (rdfstats.get_stats_results()['a69disjointproperties']['min_disjoint'], 2.0)

    def test_max(self):
        uri = 'file://' + testfile_path + 'disjointProperties.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A69DisjointProperties])
        rdfstats.start_statistics()
        self.assertEqual (rdfstats.get_stats_results()['a69disjointproperties']['max_disjoint'], 4.0)