
from ShapeQualifiedValueDetector import ShapeQualifiedValueDetector

class ShapeQualifiedValueDetectorSHACLQualifiedValue(ShapeQualifiedValueDetector):
    """
    This class implements the detection of the constraint sh:qualifiedValueShape.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ShapeQualifiedValueDetectorSHACLQualifiedValue, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#qualifiedValueShape':
            self.number += 1

    def getName(self):
        return "shapeQualifiedValueLODStatsDetectorSHACLQualifiedValue"

    def getVersion(self):
        return "shapeQualifiedValueLODStatsDetectorSHACLQualifiedValue-v1"

    def compute(self):
        self.setNumberShapeQualifiedValue(self.number)


