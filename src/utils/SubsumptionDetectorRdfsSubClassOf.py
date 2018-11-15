
from SubsumptionDetector import SubsumptionDetector
from numpy import median
from utils import util_functions

class SubsumptionDetectorRdfsSubClassOf(SubsumptionDetector):
    """
    This class implements the detection of the rdfs:subClassOf Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(SubsumptionDetectorRdfsSubClassOf, self).__init__()
        self.graph = {}
        self.c = 0
        self.roots = set()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2000/01/rdf-schema#subClassOf':
            # Keep track of potential roots
            self.roots.add(o)
            # remove every subclass from potential roots
            if s in self.roots:
                self.roots.remove(s)
            if o in self.graph:
                self.graph[o].append(s)
            else:
                self.graph[o] = [s]
            self.c += 1

    def getName(self):
        return "RdfsSubClassOf"

    def getVersion(self):
        return "RdfsSubClassOf-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):

        hierarchies_depths = util_functions.compute_depths(self.graph, self.roots)

        self.results['amount_hierarchies'] = len(hierarchies_depths)
        self.results['amount_subclasses'] = self.c
        average_depth=sum(hierarchies_depths) / float(len(hierarchies_depths))
        self.results['median_depth'] = median(hierarchies_depths)

        self.setAll(amount_hierarchies=len(hierarchies_depths),
                    amount_subclasses=self.c,
                    average=average_depth,
                    median=median(hierarchies_depths),
                    min=min(hierarchies_depths),
                    max=max(hierarchies_depths))


