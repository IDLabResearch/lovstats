
from LogicalConjunctionDetector import LogicalConjunctionDetector

class LogicalConjunctionDetectorSHACLAnd(LogicalConjunctionDetector):
    """
    This class implements the detection of the conjunction constraint sh:and.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(LogicalConjunctionDetectorSHACLAnd, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#and':
            self.number += 1

    def getName(self):
        return "logicalConjunctionLODStatsDetectorSHACLAnd"

    def getVersion(self):
        return "logicalConjunctionLODStatsDetectorSHACLAnd-v1"

    def compute(self):
        self.setNumberLogicalConjunction(self.number)


