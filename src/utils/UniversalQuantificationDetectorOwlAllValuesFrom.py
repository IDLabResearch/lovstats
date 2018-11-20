
from UniversalQuantificationDetector import UniversalQuantificationDetector

class UniversalQuantificationDetectorOwlAllValuesFrom(UniversalQuantificationDetector):
    """
    This class implements the detection of the owl:allValuesFrom Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(UniversalQuantificationDetectorOwlAllValuesFrom, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#allValuesFrom':
            self.amount += 1

    def getName(self):
        return "OwlAllValuesFrom"

    def getVersion(self):
        return "OwlAllValuesFrom-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountUniversalQuantification(self.amount)


