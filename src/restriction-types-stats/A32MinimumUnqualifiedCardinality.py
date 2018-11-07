from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SimplePropertyStats import SimplePropertyStats

class A32MinimumUnqualifiedCardinality(RDFStatInterface):
    """Amount of owl:minCardinality statements"""

    def __init__(self, results):
        super(A32MinimumUnqualifiedCardinality, self).__init__(results)
        self.c = 0
        self.propertyStats = SimplePropertyStats()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2002/07/owl#minCardinality':
            self.c += 1

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results['amount_unqualified_min_cardinality'] = self.c