
from PropertyPairLessThanDetector import PropertyPairLessThanDetector

class PropertyPairLessThanDetectorSHACLLessThan(PropertyPairLessThanDetector):
    """
    This class implements the detection of the less-than property pair constraint sh:lessThan.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyPairLessThanDetectorSHACLLessThan, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#lessThan':
            self.number += 1

    def getName(self):
        return "propertyPairLessThanLODStatsDetectorSHACLLessThan"

    def getVersion(self):
        return "propertyPairLessThanLODStatsDetectorSHACLLessThan-v1"

    def compute(self):
        self.setNumberPropertyPairLessThan(self.number)


