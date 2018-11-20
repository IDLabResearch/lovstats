from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.IrreflexiveObjectPropertiesDetectorOwlIrreflexiveProperty import IrreflexiveObjectPropertiesDetectorOwlIrreflexiveProperty
from utils import util_functions

class A64IrreflexiveObjectProperties(RDFStatInterface):
    """Amount of owl:IrreflexiveProperty statements"""

    def __init__(self, results):
        super(A64IrreflexiveObjectProperties, self).__init__(results)
        self.detectors = [IrreflexiveObjectPropertiesDetectorOwlIrreflexiveProperty()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)