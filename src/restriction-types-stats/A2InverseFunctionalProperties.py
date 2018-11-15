
from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.InverseFunctionalPropertyDetectorOwlInverseFunctionalProperty import InverseFunctionalPropertyDetectorOwlInverseFunctionalProperty
from utils import utils


class A2InverseFunctionalProperties(RDFStatInterface):
    """Amount of owl:FunctionalProperty statements"""

    def __init__(self, results):
        super(A2InverseFunctionalProperties, self).__init__(results)
        self.detectors = [InverseFunctionalPropertyDetectorOwlInverseFunctionalProperty()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = utils.gather_results(self.detectors)