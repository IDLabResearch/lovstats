
from StringMaxLengthDetector import StringMaxLengthDetector

class StringMaxLengthDetectorSHACLMaxLength(StringMaxLengthDetector):
    """
    This class implements the detection of the maximum string length constraint sh:maxLength.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(StringMaxLengthDetectorSHACLMaxLength, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#maxLength':
            self.number += 1

    def getName(self):
        return "stringMaxLengthLODStatsDetectorSHACLMaxLength"

    def getVersion(self):
        return "stringMaxLengthLODStatsDetectorSHACLMaxLength-v1"

    def compute(self):
        self.setNumberStringMaxLength(self.number)


