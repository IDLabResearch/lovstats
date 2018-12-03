
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT
from RestrictionTypeDetector import MEASURE_OCCURRENCE

class MinUnqualifiedCardinalityDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of minimum unqualified cardinality expressions.
    It defines the statistical metric amount.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(MinUnqualifiedCardinalityDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def getRestrictionType(self):
        return "minimumUnqualifiedCardinality"

    def setAmountUnqualifiedMinCardinality(self, amount):
        self.addResult(MEASURE_OCCURRENCE, amount, TYPE_INT)
