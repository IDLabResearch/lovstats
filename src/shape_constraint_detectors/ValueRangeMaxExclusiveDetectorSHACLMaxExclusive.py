
from ValueRangeMaxExclusiveDetector import ValueRangeMaxExclusiveDetector

class ValueRangeMaxExclusiveDetectorSHACLMaxExclusive(ValueRangeMaxExclusiveDetector):
    """
    This class implements the detection of the maximum exclusive value range constraint sh:maxExclusive.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueRangeMaxExclusiveDetectorSHACLMaxExclusive, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#maxExclusive':
            self.number += 1

    def getName(self):
        return "valueRangeMaxExclusiveLODStatsDetectorSHACLMaxExclusive"

    def getVersion(self):
        return "valueRangeMaxExclusiveLODStatsDetectorSHACLMaxExclusive-v1"

    def compute(self):
        self.setNumberValueRangeMaxExclusive(self.number)


