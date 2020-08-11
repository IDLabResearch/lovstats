
from LogicalExclusiveDisjunctionDetector import LogicalExclusiveDisjunctionDetector

class LogicalExclusiveDisjunctionDetectorSHACLXone(LogicalExclusiveDisjunctionDetector):
    """
    This class implements the detection of the exclusive conjunction constraint sh:xone.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(LogicalExclusiveDisjunctionDetectorSHACLXone, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#xone':
            self.number += 1

    def getName(self):
        return "logicalExclusiveDisjunctionLODStatsDetectorSHACLXone"

    def getVersion(self):
        return "logicalExclusiveDisjunctionLODStatsDetectorSHACLXone-v1"

    def compute(self):
        self.setNumberLogicalExclusiveDisjunction(self.number)


