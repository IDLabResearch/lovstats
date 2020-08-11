
from StringUniqueLangDetector import StringUniqueLangDetector

class StringUniqueLangDetectorSHACLUniqueLang(StringUniqueLangDetector):
    """
    This class implements the detection of the unique language constraint sh:uniqueLang.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(StringUniqueLangDetectorSHACLUniqueLang, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#uniqueLang':
            self.number += 1

    def getName(self):
        return "stringUniqueLangLODStatsDetectorSHACLUniqueLang"

    def getVersion(self):
        return "stringUniqueLangLODStatsDetectorSHACLUniqueLang-v1"

    def compute(self):
        self.setNumberStringUniqueLang(self.number)


