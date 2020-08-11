
from utils.RestrictionTypeDetector import RestrictionTypeDetector
from utils.RestrictionTypeDetector import TYPE_INT
from utils.RestrictionTypeDetector import MEASURE_OCCURRENCE

class PropertyPairLessThanDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all shape constraint statistics of less-than property pair constraints.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(PropertyPairLessThanDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def getRestrictionType(self):
        return "propertyPairLessThan"

    def setNumberPropertyPairLessThan(self, number):
        self.addResult(MEASURE_OCCURRENCE, number, TYPE_INT)
