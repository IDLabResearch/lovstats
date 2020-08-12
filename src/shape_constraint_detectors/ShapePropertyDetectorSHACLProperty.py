
from ShapePropertyDetector import ShapePropertyDetector

class ShapePropertyDetectorSHACLProperty(ShapePropertyDetector):
    """
    This class implements the detection of the constraint sh:property.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ShapePropertyDetector, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#property':
            self.number += 1

    def getName(self):
        return "shapePropertyLODStatsDetectorSHACLProperty"

    def getVersion(self):
        return "shapePropertyLODStatsDetectorSHACLProperty-v1"

    def compute(self):
        self.setNumberShapeProperty(self.number)


