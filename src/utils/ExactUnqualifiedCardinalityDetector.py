
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT
from RestrictionTypeDetector import MEASURE_OCCURRENCE

class ExactUnqualifiedCardinalityDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of exact unqualified cardinality expressions.
    It defines the statistical measure restriction type occurrence.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(ExactUnqualifiedCardinalityDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)

    def setAmountUnqualifiedExactCardinality(self, amount):
        self.addResult(MEASURE_OCCURRENCE, amount, TYPE_INT)
