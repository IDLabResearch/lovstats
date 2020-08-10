from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape-constraint-detectors.CardinalityMaxCountDetectorSHACLMaxCount import CardinalityMaxCountDetectorSHACLMaxCount
from utils import util_functions


class CardinalityMaxCountConstraint(RDFStatInterface):
    """Create statistics for maximum cardinality constraints on properties"""

    def __init__(self, results):
        super(CardinalityMaxCountConstraint, self).__init__(results)
        self.detectors = [CardinalityMaxCountDetectorSHACLMaxCount()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)