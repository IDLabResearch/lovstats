
from MaxQualifiedCardinalityDetector import MaxQualifiedCardinalityDetector

class MaxQualifiedCardinalityDetectorOwlMaxQualifiedCardinality(MaxQualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:OwlMaxQualifiedCardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(MaxQualifiedCardinalityDetectorOwlMaxQualifiedCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#maxQualifiedCardinality':
            self.amount += 1

    def getName(self):
        return "OwlMaxQualifiedCardinality"

    def getVersion(self):
        return "OwlMaxQualifiedCardinality-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountQualifiedMaxCardinality(self.amount)


