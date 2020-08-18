
from OtherValueInDetector import OtherValueInDetector

class OtherValueInDetectorSHACLValueIn(OtherValueInDetector):
    """
    This class implements the detection of the specific property value constraint (part of a provided list) sh:in.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(OtherValueInDetectorSHACLValueIn, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#in':
            self.number += 1

    def getName(self):
        return "otherValueInLODStatsDetectorSHACLValueIn"

    def getVersion(self):
        return "otherValueInLODStatsDetectorSHACLValueIn-v1"

    def compute(self):
        self.setNumberOtherValueIn(self.number)


