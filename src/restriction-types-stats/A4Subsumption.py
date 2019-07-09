from numpy import median

from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SubsumptionDetectorRdfsSubClassOf import SubsumptionDetectorRdfsSubClassOf
from utils.SubsumptionDetectorOwlSubClassOf import SubsumptionDetectorOwlSubClassOf
from utils import util_functions

class A4Subsumption(RDFStatInterface):
    """Multiple statistics regarding Subsumption,
    - Amount of subclasses
    - Amount of class hierarchies
    - hierarchy depth for each hierarchy
    - average class hierarchy depth
    - median class hierarchy depth"""

    def __init__(self, results):
        super(A4Subsumption, self).__init__(results)
        self.detectors = [SubsumptionDetectorRdfsSubClassOf(), SubsumptionDetectorOwlSubClassOf()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        for d in self.detectors:
            d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)