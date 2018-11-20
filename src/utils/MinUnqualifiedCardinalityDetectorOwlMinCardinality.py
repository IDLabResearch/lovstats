
from MinUnqualifiedCardinalityDetector import MinUnqualifiedCardinalityDetector

class MinUnqualifiedCardinalityDetectorOwlMinCardinality(MinUnqualifiedCardinalityDetector):
    """
    This class implements the detection of the rdfs:domain Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(MinUnqualifiedCardinalityDetectorOwlMinCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#minCardinality':
            self.amount += 1

    def getName(self):
        return "OwlMinCardinality"

    def getVersion(self):
        return "OwlMinCardinality-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountUnqualifiedMinCardinality(self.amount)


