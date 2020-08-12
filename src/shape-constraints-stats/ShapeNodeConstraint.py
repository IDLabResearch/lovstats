from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape_constraint_detectors.ShapeNodeDetectorSHACLNode import ShapeNodeDetectorSHACLNode
from utils import util_functions


class ShapeNodeConstraint(RDFStatInterface):
    """Create statistics for constraints that the source has to be compliant to a shape"""

    def __init__(self, results):
        super(ShapeNodeConstraint, self).__init__(results)
        self.detectors = [ShapeNodeDetectorSHACLNode()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)