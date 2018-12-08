
from LiteralRangesDetector import LiteralRangesDetector
from ListCreator import ListCreator

class LiteralRangesDetectorXsdMinMaxOwlRestriction(LiteralRangesDetector):
    """
    This class implements the detection of xsd:minInclusive or xsd:maxInclusive, xsd:minExclusive,
    xsd:maxExclusive in combination with owl:withRestrictions on a DataType,
    Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(LiteralRangesDetectorXsdMinMaxOwlRestriction, self).__init__()

        self.xsdPatterns = {}
        self.restriction_list_creator = ListCreator('http://www.w3.org/2002/07/owl#withRestrictions')

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        # Keep track of the (blank) nodes defining a literal pattern
        if p == 'http://www.w3.org/2001/XMLSchema#minInclusive' or \
            p == 'http://www.w3.org/2001/XMLSchema#maxInclusive' or \
                p == 'http://www.w3.org/2001/XMLSchema#minExclusive' or \
                p == 'http://www.w3.org/2001/XMLSchema#maxExclusive':
            self.xsdPatterns[s] = o

        # call the list creator which keeps track of all rdf:first and rdf:rest list elements
        self.restriction_list_creator.count(s, p, o, statement)

    def getName(self):
        return "literalRangesDetectorXsdMinMaxOwlRestriction"

    def getVersion(self):
        return "literalRangesLODStatsDetectorXsdMinMaxOwlRestriction-v1"

    def compute(self):
        self.restriction_list_creator.compute()
        self.list = self.restriction_list_creator.get_list()

        # We have now all the owl:withRestrictions rdf collections (rdf:first, rdf:rest construct)
        # additionally we have a list with all xsd patterns
        # now we have to find out which xsd patterns are part of the restrictions. That are our actual literal patterns
        literalRangesRestrictionCounter = 0
        for patternNodeID in self.xsdPatterns:
            if self.restriction_list_creator.one_list_contains(patternNodeID):
                literalRangesRestrictionCounter += 1

        # Currently not used
        amount_xsd_patterns = len(self.xsdPatterns)

        self.setAmountLiteralRangesRestrictions(literalRangesRestrictionCounter)


