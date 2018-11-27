
from ExactUnqualifiedCardinalityDetector import ExactUnqualifiedCardinalityDetector

class ExactUnqualifiedCardinalityDetectorOwlCardinality(ExactUnqualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:cardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ExactUnqualifiedCardinalityDetectorOwlCardinality, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#cardinality':
            self.amount += 1

    def getName(self):
        return "exactUnqualifiedCardinalityDetectorOwlCardinality"

    def getVersion(self):
        return "exactUnqualifiedCardinalityDetectorOwlCardinality-v1"

    def compute(self):
        self.setAmountUnqualifiedExactCardinality(self.amount)


