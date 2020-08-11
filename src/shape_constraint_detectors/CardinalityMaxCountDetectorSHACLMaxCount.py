
from CardinalityMaxCountDetector import CardinalityMaxCountDetector

class CardinalityMaxCountDetectorSHACLMaxCount(CardinalityMaxCountDetector):
    """
    This class implements the detection of the cardinality constraint sh:maxCount.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(CardinalityMaxCountDetectorSHACLMaxCount, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#maxCount':
            self.number += 1

    def getName(self):
        return "cardinalityMaxCountLODStatsDetectorSHACLMaxCount"

    def getVersion(self):
        return "cardinalityMaxCountLODStatsDetectorSHACLMaxCount-v1"

    def compute(self):
        self.setNumberCardinalityMaxCount(self.number)


