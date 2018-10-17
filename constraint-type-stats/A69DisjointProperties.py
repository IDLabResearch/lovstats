from lodstats.stats.RDFStatInterface import RDFStatInterface
from pprint import pprint
from numpy import median
import utils

class A69DisjointProperties(RDFStatInterface):
    """Multiple statistics regarding Subsumption,
    - Amount of subclasses
    - Amount of class hierarchies
    - hierarchy depth for each hierarchy
    - average class hierarchy depth
    - median class hierarchy depth"""

    def __init__(self, results):
        super(A69DisjointProperties, self).__init__(results)
        self.properties = {}
        self.c = 0
        self.avg_disjoint = self.results['avg_disjoint'] = 0
        self.median_disjoint = self.results['median_disjoint'] = 0
        self.min_disjoint = self.results['min_disjoint'] = 0
        self.max_disjoint = self.results['max_disjoint'] = 0
        self.amount_disjoint_properties = self.results["amount_disjoint_properties"] = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2002/07/owl#propertyDisjointWith':

            if s in self.properties:
                self.properties[s].append(o)
                if len(self.properties[s]) > self.max_disjoint:
                    self.max_disjoint = len(self.properties[s])
            else:
                self.properties[s] = [o]
            self.c += 1

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):

        self.min_disjoint = self.max_disjoint
        disjointPropertiesLengths = []
        for property in self.properties:
            # find the minimum amount of properties a property is disjoint with
            current_length = len(self.properties[property])
            if current_length < self.min_disjoint:
                self.min_disjoint = current_length
            disjointPropertiesLengths.append(current_length)

        self.results['amount_disjoint_properties'] = self.c
        self.results['avg_disjoint'] = sum(disjointPropertiesLengths)/ float(len(disjointPropertiesLengths))
        self.results['median_disjoint'] = median(disjointPropertiesLengths)
        self.results['min_disjoint'] = self.min_disjoint
        self.results['max_disjoint'] = self.max_disjoint