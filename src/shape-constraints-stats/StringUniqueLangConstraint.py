from lodstats.stats.RDFStatInterface import RDFStatInterface
from shape-constraint-detectors.StringUniqueLangDetectorSHACLUniqueLang import StringUniqueLangDetectorSHACLUniqueLang
from utils import util_functions


class StringUniqueLangConstraint(RDFStatInterface):
    """Create statistics for uniquely used language on specific property values"""

    def __init__(self, results):
        super(StringUniqueLangConstraint, self).__init__(results)
        self.detectors = [StringUniqueLangDetectorSHACLUniqueLang()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)