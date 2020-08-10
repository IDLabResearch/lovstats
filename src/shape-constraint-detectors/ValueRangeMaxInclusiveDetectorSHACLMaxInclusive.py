
from ValueRangeMaxInclusiveDetector import ValueRangeMaxInclusiveDetector

class ValueRangeMaxInclusiveDetectorSHACLMaxInclusive(ValueRangeMaxInclusiveDetector):
    """
    This class implements the detection of the maximum inclusive value range constraint sh:maxInclusive.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueRangeMaxInclusiveDetectorSHACLMaxInclusive, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#maxInclusive':
            self.number += 1

    def getName(self):
        return "valueRangeMaxInclusiveLODStatsDetectorSHACLMaxInclusive"

    def getVersion(self):
        return "valueRangeMaxInclusiveLODStatsDetectorSHACLMaxInclusive-v1"

    def compute(self):
        self.setNumberValueRangeMaxInclusive(self.number)


