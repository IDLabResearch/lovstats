
from PropertyPairEqualsDetector import PropertyPairEqualsDetector

class PropertyPairEqualsDetectorSHACLEquals(PropertyPairEqualsDetector):
    """
    This class implements the detection of the equals property pair constraint sh:equals.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyPairEqualsDetectorSHACLEquals, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#equals':
            self.number += 1

    def getName(self):
        return "propertyPairEqualsLODStatsDetectorSHACLEquals"

    def getVersion(self):
        return "propertyPairEqualsLODStatsDetectorSHACLEquals-v1"

    def compute(self):
        self.setNumberPropertyPairEquals(self.number)


