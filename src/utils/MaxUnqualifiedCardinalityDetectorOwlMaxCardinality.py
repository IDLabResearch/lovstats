
from MaxUnqualifiedCardinalityDetector import MaxUnqualifiedCardinalityDetector

class MaxUnqualifiedCardinalityDetectorOwlMaxCardinality(MaxUnqualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:maxCardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(MaxUnqualifiedCardinalityDetectorOwlMaxCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#maxCardinality':
            self.amount += 1

    def getName(self):
        return "OwlMaxCardinality"

    def getVersion(self):
        return "OwlMaxCardinality-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountUnqualifiedMaxCardinality(self.amount)

