
from utils.RestrictionTypeDetector import RestrictionTypeDetector
from utils.RestrictionTypeDetector import TYPE_INT
from utils.RestrictionTypeDetector import MEASURE_OCCURRENCE

class OtherValueInDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all statistics about specific property value constraints, value part of a provided list.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(OtherValueInDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def getRestrictionType(self):
        return "otherValueIn"

    def setNumberOtherValueIn(self, number):
        self.addResult(MEASURE_OCCURRENCE, number, TYPE_INT)
