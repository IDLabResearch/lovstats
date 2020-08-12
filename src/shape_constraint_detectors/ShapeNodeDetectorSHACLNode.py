
from ShapeNodeDetector import ShapeNodeDetector

class ShapeNodeDetectorSHACLNode(ShapeNodeDetector):
    """
    This class implements the detection of the constraint sh:node.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ShapeNodeDetectorSHACLNode, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#node':
            self.number += 1

    def getName(self):
        return "shapeNodeLODStatsDetectorSHACLNode"

    def getVersion(self):
        return "shapeNodeLODStatsDetectorSHACLNode-v1"

    def compute(self):
        self.setNumberShapeNode(self.number)


