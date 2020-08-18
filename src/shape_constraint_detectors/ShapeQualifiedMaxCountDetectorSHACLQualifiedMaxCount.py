
from ShapeQualifiedMaxCountDetector import ShapeQualifiedMaxCountDetector

class ShapeQualifiedMaxCountDetectorSHACLQualifiedMaxCount(ShapeQualifiedMaxCountDetector):
    """
    This class implements the detection of the constraint sh:qualifiedMaxCount.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ShapeQualifiedMaxCountDetectorSHACLQualifiedMaxCount, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#qualifiedMaxCount':
            self.number += 1

    def getName(self):
        return "shapeQualifiedMaxCountLODStatsDetectorSHACLQualifiedMaxCount"

    def getVersion(self):
        return "shapeQualifiedMaxCountLODStatsDetectorSHACLQualifiedMaxCount-v1"

    def compute(self):
        self.setNumberShapeQualifiedMaxCount(self.number)


