
from PropertyPairDisjointDetector import PropertyPairDisjointDetector

class PropertyPairDisjointDetectorSHACLDisjoint(PropertyPairDisjointDetector):
    """
    This class implements the detection of the disjoint property pair constraint sh:disjoint.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyPairDisjointDetectorSHACLDisjoint, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#disjoint':
            self.number += 1

    def getName(self):
        return "propertyPairDisjointLODStatsDetectorSHACLDisjoint"

    def getVersion(self):
        return "propertyPairDisjointLODstatsDetectorSHACLDisjoint-v1"

    def compute(self):
        self.setNumberPropertyPairDisjoint(self.number)


