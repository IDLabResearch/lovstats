
from CardinalityMinCountDetector import CardinalityMinCountDetector

class CardinalityMinCountDetectorSHACLMinCount(CardinalityMinCountDetector):
    """
    This class implements the detection of the cardinality constraint sh:minCount.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(CardinalityMinCountDetectorSHACLMinCount, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#minCount':
            self.number += 1

    def getName(self):
        return "cardinalityMinCountLODStatsDetectorSHACLMinCount"

    def getVersion(self):
        return "cardinalityMinCountLODStatsDetectorSHACLMinCount-v1"

    def compute(self):
        self.setNumberCardinalityMinCount(self.number)


