
from TargetNodeTargetDetector import TargetNodeTargetDetector

class TargetNodeTargetDetectorSHACLTargetNode(TargetNodeTargetDetector):
    """
    This class implements the detection of shapes applying on individuals declared via sh:targetNode.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(TargetNodeTargetDetectorSHACLTargetNode, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#targetNode':
            self.number += 1

    def getName(self):
        return "targetNodeTargetLODStatsDetectorSHACLTargetNode"

    def getVersion(self):
        return "targetNodeTargetLODStatsDetectorSHACLTargetNode-v1"

    def compute(self):
        self.setNumberTargetNodeTarget(self.number)


