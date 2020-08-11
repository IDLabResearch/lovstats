
from ValueRangeMinInclusiveDetector import ValueRangeMinInclusiveDetector

class ValueRangeMinInclusiveDetectorSHACLMinInclusive(ValueRangeMinInclusiveDetector):
    """
    This class implements the detection of the minimum inclusive value range constraint sh:minInclusive.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueRangeMinInclusiveDetectorSHACLMinInclusive, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#minInclusive':
            self.number += 1

    def getName(self):
        return "valueRangeMinInclusiveLODStatsDetectorSHACLMinInclusive"

    def getVersion(self):
        return "valueRangeMinInclusiveLODStatsDetectorSHACLMinInclusive-v1"

    def compute(self):
        self.setNumberValueRangeMinInclusive(self.number)


