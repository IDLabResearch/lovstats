
from StringPatternDetector import StringPatternDetector

class StringPatternDetectorSHACLPattern(StringPatternDetector):
    """
    This class implements the detection of the string pattern constraint sh:pattern for literals.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(StringPatternDetectorSHACLPattern, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#pattern':
            self.number += 1

    def getName(self):
        return "stringPatternLODStatsDetectorSHACLPattern"

    def getVersion(self):
        return "stringPatternLODStatsDetectorSHACLPattern-v1"

    def compute(self):
        self.setNumberStringPattern(self.number)


