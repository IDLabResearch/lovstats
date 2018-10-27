from lodstats.stats.RDFStatInterface import RDFStatInterface
from utils.ListCreator import ListCreator
from pprint import pprint

class A20LiteralPatternMatching(RDFStatInterface):
    """Amount of owl:AsymmetricProperty statements"""

    def __init__(self, results):
        super(A20LiteralPatternMatching, self).__init__(results)
        self.xsdPatterns = {}

        self.restriction_list_creator = ListCreator('http://www.w3.org/2002/07/owl#withRestrictions')

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        # Keep track of the (blank) nodes defining a literal pattern
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/2001/XMLSchema#pattern':
            self.xsdPatterns[s] = o

        # call the list creator which keeps track of all rdf:first and rdf:rest list elements
        self.restriction_list_creator.count(s, p, o, statement)

    def voidify(self, void_model, dataset):
        pass

    def sparql(self, endpoint):
        pass

    def postproc(self):
        self.restriction_list_creator.compute()
        self.list = self.restriction_list_creator.get_list()

        pprint(self.xsdPatterns)
        pprint(self.list)
        # We have now all the owl:withRestrictions rdf collections (rdf:first, rdf:rest construct)
        # additionally we have a list with all xsd patterns
        # now we have to find out which xsd patterns are part of the restrictions. That are our actual literal patterns
        literalPatternRestrictionCounter = 0
        for patternNodeID in self.xsdPatterns:
            if self.restriction_list_creator.one_list_contains(patternNodeID):
                literalPatternRestrictionCounter += 1

        self.results['amount_xsd_patterns'] = len(self.xsdPatterns)
        self.results['amount_literal_patterns'] = literalPatternRestrictionCounter