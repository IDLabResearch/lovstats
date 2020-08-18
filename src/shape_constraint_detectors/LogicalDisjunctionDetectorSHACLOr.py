
from LogicalDisjunctionDetector import LogicalDisjunctionDetector

class LogicalDisjunctionDetectorSHACLOr(LogicalDisjunctionDetector):
    """
    This class implements the detection of the disjunction constraint sh:or.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(LogicalDisjunctionDetectorSHACLOr, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#or':
            self.number += 1

    def getName(self):
        return "logicalDisjunctionLODStatsDetectorSHACLOr"

    def getVersion(self):
        return "logicalDisjunctionLODStatsDetectorSHACLOr-v1"

    def compute(self):
        self.setNumberLogicalDisjunction(self.number)


