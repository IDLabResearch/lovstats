from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.AsymmetricPropertiesDetectorOwlAsymmetricProperty import AsymmetricPropertiesDetectorOwlAsymmetricProperty
from utils import util_functions

class A57AsymmetricProperties(RDFStatInterface):
    """Amount of owl:AsymmetricProperty statements"""

    def __init__(self, results):
        super(A57AsymmetricProperties, self).__init__(results)
        self.detectors = [AsymmetricPropertiesDetectorOwlAsymmetricProperty()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)