
from OtherHasValueDetector import OtherHasValueDetector

class OtherHasValueDetectorSHACLHasValue(OtherHasValueDetector):
    """
    This class implements the detection of the specific value constraint sh:hasValue.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(OtherHasValueDetectorSHACLHasValue, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#hasValue':
            self.number += 1

    def getName(self):
        return "otherHasValueLODStatsDetectorSHACLHasValue"

    def getVersion(self):
        return "otherHasValueLODStatsDetectorSHACLHasValue-v1"

    def compute(self):
        self.setNumberOtherHasValue(self.number)


