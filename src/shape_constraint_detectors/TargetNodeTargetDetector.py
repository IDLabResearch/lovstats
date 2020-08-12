
from utils.RestrictionTypeDetector import RestrictionTypeDetector
from utils.RestrictionTypeDetector import TYPE_INT
from utils.RestrictionTypeDetector import MEASURE_OCCURRENCE

class TargetNodeTargetDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all statistics of shapes applying on individuals.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(TargetNodeTargetDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def getRestrictionType(self):
        return "targetNodeTarget"

    def setNumberTargetNodeTarget(self, number):
        self.addResult(MEASURE_OCCURRENCE, number, TYPE_INT)
