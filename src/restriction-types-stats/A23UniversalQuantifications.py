from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.UniversalQuantificationDetectorOwlAllValuesFrom import UniversalQuantificationDetectorOwlAllValuesFrom
from utils.SimplePropertyStats import SimplePropertyStats
from utils import util_functions

class A23UniversalQuantifications(RDFStatInterface):
    """Create statistics for universal quantifications"""

    def __init__(self, results):
        super(A23UniversalQuantifications, self).__init__(results)
        self.detectors = [UniversalQuantificationDetectorOwlAllValuesFrom()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)