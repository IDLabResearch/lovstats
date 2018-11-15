
from RestrictionTypeDetector import RestrictionTypeDetector

class DisjointClassDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of disjoint class expressions.
    It defines the statistical metrics amount, average, median, min and max.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(DisjointClassDetector, self).__init__()
        self.addResult("amount", 0, "int")
        self.addResult("average", 0.0, "float")
        self.addResult("median", 0.0, "float")
        self.addResult("min", 0, "int")
        self.addResult("max", 0, "int")

    def setAmountDisjointProperties(self, amount):
        self.addResult("amount", amount, "int")

    def setAverageDisjoint(self, average):
        self.addResult("average", average, "float")

    def setMedianDisjoint(self, median):
        self.addResult("median", median, "float")

    def setMinDisjoint(self, min):
        self.addResult("min", min, "int")

    def setMaxDisjoint(self, max):
        self.addResult("max", max, "int")

    def setAll(self, amount, average, median, min, max):
        self.addResult("amount", amount, "int")
        self.addResult("average", average, "float")
        self.addResult("median", median, "float")
        self.addResult("min", min, "int")
        self.addResult("max", max, "int")