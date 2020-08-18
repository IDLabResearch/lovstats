
from TargetClassTargetDetector import TargetClassTargetDetector

class TargetClassTargetDetectorSHACLTargetClass(TargetClassTargetDetector):
    """
    This class implements the detection of shapes applying on instances of classes declared via sh:targetClass.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(TargetClassTargetDetectorSHACLTargetClass, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#targetClass':
            self.number += 1

    def getName(self):
        return "targetClassTargetLODStatsDetectorSHACLTargetClass"

    def getVersion(self):
        return "targetClassTargetLODStatsDetectorSHACLTargetClass-v1"

    def compute(self):
        self.setNumberTargetClassTarget(self.number)


