
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT
from RestrictionTypeDetector import TYPE_FLOAT
from RestrictionTypeDetector import MEASURE_OCCURRENCE
from RestrictionTypeDetector import MEASURE_HIERARCHY_OCCURRENCE
from RestrictionTypeDetector import MEASURE_HIERARCHY_MIN_DEPTH
from RestrictionTypeDetector import MEASURE_HIERARCHY_MAX_DEPTH
from RestrictionTypeDetector import MEASURE_HIERARCHY_AVERAGE_DEPTH
from RestrictionTypeDetector import MEASURE_HIERARCHY_MEDIAN_DEPTH

class SubsumptionDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of subsumption expressions.
    It defines the statistical metrics amount, average, median, min and max.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """

    def __init__(self):
        super(SubsumptionDetector, self).__init__()

        #self.addResult(MEASURE_HIERARCHY_OCCURRENCE, 0, TYPE_INT)
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)
        #self.addResult(MEASURE_HIERARCHY_AVERAGE_DEPTH, 0.0, TYPE_FLOAT)
        #self.addResult(MEASURE_HIERARCHY_MEDIAN_DEPTH, 0.0, TYPE_FLOAT)
        #self.addResult(MEASURE_HIERARCHY_MIN_DEPTH, 0, TYPE_INT)
        #self.addResult(MEASURE_HIERARCHY_MAX_DEPTH, 0, TYPE_INT)

    def getRestrictionType(self):
        return "subsumption"

    def setAmountHierarchies(self, amount):
        self.addResult(MEASURE_HIERARCHY_OCCURRENCE, amount, TYPE_INT)

    def setAmountSubclasses(self, amount):
        self.addResult(MEASURE_OCCURRENCE, amount, TYPE_INT)

    def setAverageHierarchyDepth(self, average):
        self.addResult(MEASURE_HIERARCHY_AVERAGE_DEPTH, average, TYPE_FLOAT)

    def setMedianHierarchyDepth(self, median):
        self.addResult(MEASURE_HIERARCHY_MEDIAN_DEPTH, median, TYPE_FLOAT)

    def setMinHierarchyDepth(self, min):
        self.addResult(MEASURE_HIERARCHY_MIN_DEPTH, min, TYPE_INT)

    def setMaxHierarchyDepth(self, max):
        self.addResult(MEASURE_HIERARCHY_MAX_DEPTH, max, TYPE_INT)

    def setAll(self, amount_hierarchies, amount_subclasses, average, median, min, max):
        self.addResult(MEASURE_HIERARCHY_OCCURRENCE, amount_hierarchies, TYPE_INT)
        self.addResult(MEASURE_OCCURRENCE, amount_subclasses, TYPE_INT)
        self.addResult(MEASURE_HIERARCHY_AVERAGE_DEPTH, average, TYPE_FLOAT)
        self.addResult(MEASURE_HIERARCHY_MEDIAN_DEPTH, median, TYPE_FLOAT)
        self.addResult(MEASURE_HIERARCHY_MIN_DEPTH, min, TYPE_INT)
        self.addResult(MEASURE_HIERARCHY_MAX_DEPTH, max, TYPE_INT)