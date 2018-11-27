
from MinQualifiedCardinalityDetector import MinQualifiedCardinalityDetector

class MinQualifiedCardinalityDetectorOwlMinQualifiedCardinality(MinQualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:OwlMinQualifiedCardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(MinQualifiedCardinalityDetectorOwlMinQualifiedCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#minQualifiedCardinality':
            self.amount += 1

    def getName(self):
        return "minimumQualifiedCardinalityDetector"

    def getVersion(self):
        return "minimumQualifiedCardinalityDetector-v1"

    def compute(self):
        self.setAmountQualifiedMinCardinality(self.amount)


