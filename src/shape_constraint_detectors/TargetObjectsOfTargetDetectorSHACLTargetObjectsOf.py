
from TargetObjectsOfTargetDetector import TargetObjectsOfTargetDetector

class TargetObjectsOfTargetDetectorSHACLTargetObjectsOf(TargetObjectsOfTargetDetector):
    """
    This class implements the detection of shapes applying on objects of properties declared via sh:targetObjectsOf.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(TargetObjectsOfTargetDetectorSHACLTargetObjectsOf, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#targetObjectsOf':
            self.number += 1

    def getName(self):
        return "targetObjectsOfTargetLODStatsDetectorSHACLTargetObjectsOf"

    def getVersion(self):
        return "targetObjectsOfTargetLODStatsDetectorSHACLTargetObjectsOf-v1"

    def compute(self):
        self.setNumberTargetObjectsOfTarget(self.number)


