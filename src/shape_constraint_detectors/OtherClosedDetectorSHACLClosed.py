
from OtherClosedDetector import OtherClosedDetector

class OtherClosedDetectorSHACLClosed(OtherClosedDetector):
    """
    This class implements the detection of the closed shape constraint sh:closed.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(OtherClosedDetectorSHACLClosed, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#closed' and o == "true":
            self.number += 1

    def getName(self):
        return "otherClosedLODStatsDetectorSHACLClosed"

    def getVersion(self):
        return "otherClosedLODStatsDetectorSHACLClosed-v1"

    def compute(self):
        self.setNumberOtherClosed(self.number)


