import unittest

import sys
import helpers
sys.path.append('../LODStats')
sys.path.append('../src/restriction-types-stats')
from A20LiteralPatternMatching import A20LiteralPatternMatching
import lodstats
from lodstats import RDFStats

testfile_path = helpers.resources_path

class TestA20LiteralPatternMatching(unittest.TestCase):

    def setUp(self):
        lodstats.stats.stats_to_do = []
        lodstats.stats.results = {}

    def test_amount_patterns(self):
        uri = 'file://' + testfile_path + 'literalPatternMatching.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A20LiteralPatternMatching])
        rdfstats.start_statistics()
        self.assertEqual(rdfstats.get_stats_results()['a20literalpatternmatching']['amount_literal_patterns'], 1)

    def test_amount_pattern_restrictions(self):
        uri = 'file://' + testfile_path + 'literalPatternMatching.nt'
        rdfstats = RDFStats(uri, format="nt", stats=[A20LiteralPatternMatching])
        rdfstats.start_statistics()
        self.assertEqual (rdfstats.get_stats_results()['a20literalpatternmatching']['amount_xsd_patterns'], 2)
