
from StringMinLengthDetector import StringMinLengthDetector

class StringMinLengthDetectorSHACLMinLength(StringMinLengthDetector):
    """
    This class implements the detection of the minimum string length constraint sh:minLength.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(StringMinLengthDetectorSHACLMinLength, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#minLength':
            self.number += 1

    def getName(self):
        return "stringMinLengthLODStatsDetectorSHACLMinLength"

    def getVersion(self):
        return "stringMinLengthLODStatsDetectorSHACLMinLength-v1"

    def compute(self):
        self.setNumberStringMinLength(self.number)


