
from ExactQualifiedCardinalityDetector import ExactQualifiedCardinalityDetector

class ExactQualifiedCardinalityDetectorOwlCardinality(ExactQualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:qualifiedCardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ExactQualifiedCardinalityDetectorOwlCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#qualifiedCardinality':
            self.amount += 1

    def getName(self):
        return "exactQualifiedCardinalityDetectorOwlCardinality"

    def getVersion(self):
        return "exactQualifiedCardinalityLODStatsDetectorOwlCardinality-v1"

    def compute(self):
        self.setAmountQualifiedExactCardinality(self.amount)


