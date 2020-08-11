
from ValueTypeNodeKindDetector import ValueTypeNodeKindDetector

class ValueTypeNodeKindDetectorSHACLNodeKind(ValueTypeNodeKindDetector):
    """
    This class implements the detection of the value constraint sh:nodeKind.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueTypeNodeKindDetectorSHACLNodeKind, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#nodeKind':
            self.number += 1

    def getName(self):
        return "valueTypeNodeKindSHACLNodeKind"

    def getVersion(self):
        return "valueTypeNodeKindLODStatsDetectorSHACLNodeKind-v1"

    def compute(self):
        self.setNumberValueTypeNodeKind(self.number)


