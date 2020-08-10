
from ValueRangeMinExclusiveDetector import ValueRangeMinExclusiveDetector

class ValueRangeMinExclusiveDetectorSHACLMinExclusive(ValueRangeMinExclusiveDetector):
    """
    This class implements the detection of the minimum exclusive value range constraint sh:minExclusive.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueRangeMinExclusiveDetectorSHACLMinExclusive, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#minExclusive':
            self.number += 1

    def getName(self):
        return "valueRangeMinExclusiveLODStatsDetectorSHACLMinExclusive"

    def getVersion(self):
        return "valueRangeMinExclusiveLODStatsDetectorSHACLMinExclusive-v1"

    def compute(self):
        self.setNumberValueRangeMinExclusive(self.number)


