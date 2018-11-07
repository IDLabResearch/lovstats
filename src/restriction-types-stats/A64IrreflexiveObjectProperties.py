from lodstats.stats.RDFStatInterface import RDFStatInterface

class A64IrreflexiveObjectProperties(RDFStatInterface):
    """Amount of owl:IrreflexiveProperty statements"""

    def __init__(self, results):
        super(A64IrreflexiveObjectProperties, self).__init__(results)
        self.c = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' and \
                        o == 'http://www.w3.org/2002/07/owl#IrreflexiveProperty':
            self.c += 1

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.results['amount_irreflexive_properties'] = self.c