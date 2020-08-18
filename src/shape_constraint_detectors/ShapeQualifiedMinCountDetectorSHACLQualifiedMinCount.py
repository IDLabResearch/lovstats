
from ShapeQualifiedMinCountDetector import ShapeQualifiedMinCountDetector

class ShapeQualifiedMinCountDetectorSHACLQualifiedMinCount(ShapeQualifiedMinCountDetector):
    """
    This class implements the detection of the constraint sh:qualifiedMinCount.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ShapeQualifiedMinCountDetectorSHACLQualifiedMinCount, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#qualifiedMinCount':
            self.number += 1

    def getName(self):
        return "shapeQualifiedMinCountLODStatsDetectorSHACLQualifiedMinCount"

    def getVersion(self):
        return "shapeQualifiedMinCountLODStatsDetectorSHACLQualifiedMinCount-v1"

    def compute(self):
        self.setNumberShapeQualifiedMinCount(self.number)


