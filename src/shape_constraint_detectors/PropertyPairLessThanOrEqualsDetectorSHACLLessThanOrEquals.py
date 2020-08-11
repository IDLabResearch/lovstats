
from PropertyPairLessThanOrEqualsDetector import PropertyPairLessThanOrEqualsDetector

class PropertyPairLessThanOrEqualsDetectorSHACLLessThanOrEquals(PropertyPairLessThanOrEqualsDetector):
    """
    This class implements the detection of the less-than-or-equals property pair constraint sh:lessThanOrEquals.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyPairLessThanOrEqualsDetectorSHACLLessThanOrEquals, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#lessThanOrEquals':
            self.number += 1

    def getName(self):
        return "propertyPairLessThanOrEqualsLODStatsDetectorSHACLLessThanOrEquals"

    def getVersion(self):
        return "propertyPairLessThanOrEqualsLODStatsDetectorSHACLLessThanOrEquals-v1"

    def compute(self):
        self.setNumberPropertyPairLessThanOrEquals(self.number)


