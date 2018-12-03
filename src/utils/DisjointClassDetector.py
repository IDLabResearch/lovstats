
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT
from RestrictionTypeDetector import TYPE_FLOAT
from RestrictionTypeDetector import MEASURE_OCCURRENCE

class DisjointClassDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of disjoint class expressions.
    It defines the statistical metrics amount, average, median, min and max.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(DisjointClassDetector, self).__init__()
        self.addResult(MEASURE_OCCURRENCE, 0, TYPE_INT)
        #self.addResult("average", 0.0, TYPE_FLOAT)
        #self.addResult("median", 0.0, TYPE_FLOAT)
        #self.addResult("min", 0, TYPE_INT)
        #self.addResult("max", 0, TYPE_INT)

    def getRestrictionType(self):
        return "disjointClasses"

    def setAmountDisjointProperties(self, amount):
        self.addResult(MEASURE_OCCURRENCE, amount, TYPE_INT)

    def setAverageDisjoint(self, average):
        self.addResult("average", average, TYPE_FLOAT)

    def setMedianDisjoint(self, median):
        self.addResult("median", median, TYPE_FLOAT)

    def setMinDisjoint(self, min):
        self.addResult("min", min, TYPE_INT)

    def setMaxDisjoint(self, max):
        self.addResult("max", max, TYPE_INT)

    def setAll(self, amount, average, median, min, max):
        self.addResult(MEASURE_OCCURRENCE, amount, TYPE_INT)
        #self.addResult("average", average, TYPE_FLOAT)
        #self.addResult("median", median, TYPE_FLOAT)
        #self.addResult("min", min, TYPE_INT)
        #self.addResult("max", max, TYPE_INT)