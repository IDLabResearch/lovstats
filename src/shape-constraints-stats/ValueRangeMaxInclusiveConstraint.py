from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape-constraint-detectors.ValueRangeMaxInclusiveDetectorSHACLMaxExclusive import ValueRangeMaxInclusiveDetectorSHACLMaxInclusive
from utils import util_functions


class ValueRangeMaxInclusiveConstraint(RDFStatInterface):
    """Create statistics for maximum inclusive value range constraints on values"""

    def __init__(self, results):
        super(ValueRangeMaxInclusiveConstraint, self).__init__(results)
        self.detectors = [ValueRangeMaxInclusiveDetectorSHACLMaxInclusive()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)