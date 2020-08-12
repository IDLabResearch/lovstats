from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape_constraint_detectors.ShapePropertyDetectorSHACLProperty import ShapePropertyDetectorSHACLProperty
from utils import util_functions


class ShapePropertyConstraint(RDFStatInterface):
    """Create statistics for constraints on a property"""

    def __init__(self, results):
        super(ShapePropertyConstraint, self).__init__(results)
        self.detectors = [ShapePropertyDetectorSHACLProperty()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)