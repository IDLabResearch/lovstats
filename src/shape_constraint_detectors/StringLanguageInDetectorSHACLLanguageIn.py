
from StringLanguageInDetector import StringLanguageInDetector

class StringLanguageInDetectorSHACLLanguageIn(StringLanguageInDetector):
    """
    This class implements the detection of the language-in constraint sh:languageIn.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(StringLanguageInDetectorSHACLLanguageIn, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#languageIn':
            self.number += 1

    def getName(self):
        return "stringLanguageInLODStatsDetectorSHACLLanguageIn"

    def getVersion(self):
        return "stringLanguageInLODStatsDetectorSHACLLanguageIn-v1"

    def compute(self):
        self.setNumberStringLanguageIn(self.number)


