
from utils.RestrictionTypeDetector import RestrictionTypeDetector
from utils.RestrictionTypeDetector import TYPE_INT
from utils.RestrictionTypeDetector import MEASURE_OCCURRENCE

class PropertyPairLessThanOrEqualsDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all shape constraint statistics of less-than-or-equals property pair constraints.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(PropertyPairLessThanOrEqualsDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def getRestrictionType(self):
        return "propertyPairLessThanOrEquals"

    def setNumberPropertyPairLessThanOrEquals(self, number):
        self.addResult(MEASURE_OCCURRENCE, number, TYPE_INT)
