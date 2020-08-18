from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape_constraint_detectors.LogicalNegationDetectorSHACLNot import LogicalNegationDetectorSHACLNot
from utils import util_functions


class LogicalNegationConstraint(RDFStatInterface):
    """Create statistics for logical 'not' constraints (negations)"""

    def __init__(self, results):
        super(LogicalNegationConstraint, self).__init__(results)
        self.detectors = [LogicalNegationDetectorSHACLNot()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)