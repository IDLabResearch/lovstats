from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.MaxQualifiedCardinalityDetectorOwlMaxQualifiedCardinality import MaxQualifiedCardinalityDetectorOwlMaxQualifiedCardinality
from utils import util_functions

class A35MaximumQualifiedCardinality(RDFStatInterface):
    """Create statistics about maximum qualified cardinality"""

    def __init__(self, results):
        super(A35MaximumQualifiedCardinality, self).__init__(results)
        self.detectors = [MaxQualifiedCardinalityDetectorOwlMaxQualifiedCardinality()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)