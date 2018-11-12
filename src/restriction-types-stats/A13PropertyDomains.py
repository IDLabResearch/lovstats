from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.SimplePropertyStats import SimplePropertyStats

class A13PropertyDomains(RDFStatInterface):
    """Amount of rdfs:domain statements"""

    def __init__(self, results):
        super(A13PropertyDomains, self).__init__(results)
        self.c = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2000/01/rdf-schema#domain':
            self.c += 1

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results['amount_property_domains'] = self.c
