
from TargetSubjectsOfTargetDetector import TargetSubjectsOfTargetDetector

class TargetSubjectsOfTargetDetectorSHACLTargetSubjectsOf(TargetSubjectsOfTargetDetector):
    """
    This class implements the detection of shapes applying on subjects of properties declared via sh:targetSubjectsOf.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(TargetSubjectsOfTargetDetectorSHACLTargetSubjectsOf, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#targetSubjectsOf':
            self.number += 1

    def getName(self):
        return "targetSubjectsOfTargetLODStatsDetectorSHACLTargetSubjectsOf"

    def getVersion(self):
        return "targetSubjectsOfTargetLODStatsDetectorSHACLTargetSubjectsOf-v1"

    def compute(self):
        self.setNumberTargetSubjectsOfTarget(self.number)


