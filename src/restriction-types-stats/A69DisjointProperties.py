from numpy import median

from lodstats.stats.RDFStatInterface import RDFStatInterface
from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SimplePropertyStats import SimplePropertyStats

class A69DisjointProperties(RDFStatInterface):
    """SimplePropertyStatistics for disjoint classes"""

    def __init__(self, results):
        super(A69DisjointProperties, self).__init__(results)

        self.propertyStats = SimplePropertyStats()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2002/07/owl#propertyDisjointWith':
            self.propertyStats.count(s, o)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.propertyStats.compute()

        self.results['amount_disjoint_properties'] = self.propertyStats.getAmount()
        self.results['avg_disjoint'] = self.propertyStats.getAverage()
        self.results['median_disjoint'] = self.propertyStats.getMedian()
        self.results['min_disjoint'] = self.propertyStats.getMin()
        self.results['max_disjoint'] = self.propertyStats.getMax()