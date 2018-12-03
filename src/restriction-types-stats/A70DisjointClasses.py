from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SimplePropertyStats import SimplePropertyStats
from utils.DisjointClassDetectorOwlDisjointWith import DisjointClassDetectorOwlDisjointWith
from utils.DisjointClassDetectorOwlAllDisjointClasses import DisjointClassDetectorOwlAllDisjointClasses
from utils import util_functions

class A70DisjointClasses(RDFStatInterface):
    """Create statistics for disjoint classes"""

    def __init__(self, results):
        super(A70DisjointClasses, self).__init__(results)

        self.detectors = [DisjointClassDetectorOwlAllDisjointClasses(), DisjointClassDetectorOwlDisjointWith()]

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
            for d in self.detectors:
                d.count(s, p, o, s_blank, o_l, o_blank, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results["detectors"] = util_functions.gather_results(self.detectors)