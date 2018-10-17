from lodstats.stats.RDFStatInterface import RDFStatInterface
from pprint import pprint
from numpy import median
import utils

class C1Subsumption(RDFStatInterface):
    """Multiple statistics regarding Subsumption,
    - Amount of subclasses
    - Amount of class hierarchies
    - hierarchy depth for each hierarchy
    - average class hierarchy depth
    - median class hierarchy depth"""

    def __init__(self, results):
        super(C1Subsumption, self).__init__(results)
        self.graph = {}
        self.c = 0
        self.roots = set()
        self.avg_depth = self.results['avg_depth'] = 0
        self.median_depth = self.results['median_depth'] = 0
        self.amount_hierarchies = self.results['amount_hierarchies'] = 0
        self.amount_subclasses = self.results["amount_subclasses"] = 0

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

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):

        hierarchies_depths = utils.compute_depths(self.graph, self.roots)

        self.results['amount_hierarchies'] = len(hierarchies_depths)
        self.results['amount_subclasses'] = self.c
        self.results['avg_depth'] = sum(hierarchies_depths)/ float(len(hierarchies_depths))
        self.results['median_depth'] = median(hierarchies_depths)