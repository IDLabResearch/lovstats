from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.LiteralRangesDetectorXsdMinMaxOwlRestriction import LiteralRangesDetectorXsdMinMaxOwlRestriction
from utils import util_functions

class A17LiteralRanges(RDFStatInterface):
    """Create statistics for literal ranges"""

    def __init__(self, results):
        super(A17LiteralRanges, self).__init__(results)
        self.detectors = [LiteralRangesDetectorXsdMinMaxOwlRestriction()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)