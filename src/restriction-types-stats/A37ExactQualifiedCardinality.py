from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.ExactQualifiedCardinalityDetectorOwlCardinality import ExactQualifiedCardinalityDetectorOwlCardinality
from utils import util_functions

class A37ExactQualifiedCardinality(RDFStatInterface):
    """Create statistics about exact unqualified cardinality"""

    def __init__(self, results):
        super(A37ExactQualifiedCardinality, self).__init__(results)
        self.detectors = [ExactQualifiedCardinalityDetectorOwlCardinality()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)