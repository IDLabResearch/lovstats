from numpy import median

from lodstats.stats.RDFStatInterface import RDFStatInterface
from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SimplePropertyStats import SimplePropertyStats
from utils.DisjointPropertyDetectorOwlDisjointWith import DisjointPropertyDetectorOwlDisjointWith
from utils import utils

class A69DisjointProperties(RDFStatInterface):
    """Create statistics for disjoint properties"""

    def __init__(self, results):
        super(A69DisjointProperties, self).__init__(results)

        self.detectors = [DisjointPropertyDetectorOwlDisjointWith()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
            for d in self.detectors:
                d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = utils.gather_results(self.detectors)