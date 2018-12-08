
from ExactUnqualifiedCardinalityDetector import ExactUnqualifiedCardinalityDetector

class ExactUnqualifiedCardinalityDetectorOwlMinMax(ExactUnqualifiedCardinalityDetector):
    """
    This class implements the detection of the owl:minCardinality==owl:maxCardinality Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ExactUnqualifiedCardinalityDetectorOwlMinMax, self).__init__()
        self.minCardinalities = {}
        self.maxCardinalities = {}
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#minCardinality':
            self.minCardinalities[s] = o
        if p == 'http://www.w3.org/2002/07/owl#maxCardinality':
            self.maxCardinalities[s] = o

    def getName(self):
        return "exactUnqualifiedCardinalityDetectorOwlMinMax"

    def getVersion(self):
        return "exactUnqualifiedCardinalityLODStatsDetectorOwlMinMax-v1"

    def compute(self):
        # Reduce amount of comparisons by selecting smaller dictionary for outer loop
        outer = self.minCardinalities if len(self.minCardinalities) < len(self.maxCardinalities) else self.maxCardinalities
        inner = self.maxCardinalities if len(self.maxCardinalities) > len(self.minCardinalities) else self.minCardinalities

        for i in outer:
            if i in inner:
                if outer[i] == inner[i]:
                    self.amount += 1
        self.setAmountUnqualifiedExactCardinality(self.amount)


