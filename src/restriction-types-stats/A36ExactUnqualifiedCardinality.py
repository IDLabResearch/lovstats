from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.ExactUnqualifiedCardinalityDetectorOwlCardinality import ExactUnqualifiedCardinalityDetectorOwlCardinality
from utils.ExactUnqualifiedCardinalityDetectorOwlMinMax import ExactUnqualifiedCardinalityDetectorOwlMinMax
from utils import util_functions

class A36ExactUnqualifiedCardinality(RDFStatInterface):
    """Create statistics about exact unqualified cardinality"""

    def __init__(self, results):
        super(A36ExactUnqualifiedCardinality, self).__init__(results)
        self.detectors = [ExactUnqualifiedCardinalityDetectorOwlCardinality(), ExactUnqualifiedCardinalityDetectorOwlMinMax()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)