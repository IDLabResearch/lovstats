from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape_constraint_detectors.ShapeQualifiedMinCountDetectorSHACLQualifiedMinCount import ShapeQualifiedMinCountDetectorSHACLQualifiedMinCount
from utils import util_functions


class ShapeQualifiedMinCountConstraint(RDFStatInterface):
    """Create statistics for the constraint that the value of a minimum number of a property needs to comply to a shape"""

    def __init__(self, results):
        super(ShapeQualifiedMinCountConstraint, self).__init__(results)
        self.detectors = [ShapeQualifiedMinCountDetectorSHACLQualifiedMinCount()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)