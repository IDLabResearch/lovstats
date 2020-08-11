
from LogicalNegationDetector import LogicalNegationDetector

class LogicalNegationDetectorSHACLNot(LogicalNegationDetector):
    """
    This class implements the detection of the negation constraint sh:not.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(LogicalNegationDetectorSHACLNot, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#not':
            self.number += 1

    def getName(self):
        return "logicalNegationLODStatsDetectorSHACLNot"

    def getVersion(self):
        return "logicalNegationLODStatsDetectorSHACLNot-v1"

    def compute(self):
        self.setNumberLogicalNegation(self.number)


