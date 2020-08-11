from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape_constraint_detectors.PropertyPairDisjointDetectorSHACLDisjoint import PropertyPairDisjointDetectorSHACLDisjoint
from utils import util_functions


class PropertyPairDisjointConstraint(RDFStatInterface):
    """Create statistics for disjoint values constraints on properties"""

    def __init__(self, results):
        super(PropertyPairDisjointConstraint, self).__init__(results)
        self.detectors = [PropertyPairDisjointDetectorSHACLDisjoint()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)