
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT
from RestrictionTypeDetector import TYPE_FLOAT

class SubsumptionDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of subsumption expressions.
    It defines the statistical metrics amount, average, median, min and max.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """

    def __init__(self):
        super(SubsumptionDetector, self).__init__()
        self.key_amount_hierarchies = "amount_hierarchies"
        self.key_amount_subclasses = "amount_subclasses"
        self.key_average_depth = "average_depth"
        self.key_median_depth = "median_depth"
        self.key_min_depth = "min_depth"
        self.key_max_depth = "max_depth"

        self.addResult(self.key_amount_hierarchies, 0, TYPE_INT)
        self.addResult(self.key_amount_subclasses, 0, TYPE_INT)
        self.addResult(self.key_average_depth, 0.0, TYPE_FLOAT)
        self.addResult(self.key_median_depth, 0.0, TYPE_FLOAT)
        self.addResult(self.key_min_depth, 0, TYPE_INT)
        self.addResult(self.key_max_depth, 0, TYPE_INT)

    def setAmountHierarchies(self, amount):
        self.addResult(self.key_amount_hierarchies, amount, TYPE_INT)

    def setAmountSubclasses(self, amount):
        self.addResult(self.key_amount_subclasses, amount, TYPE_INT)

    def setAverageHierarchyDepth(self, average):
        self.addResult(self.key_average_depth, average, TYPE_FLOAT)

    def setMedianHierarchyDepth(self, median):
        self.addResult(self.key_median_depth, median, TYPE_FLOAT)

    def setMinHierarchyDepth(self, min):
        self.addResult(self.key_min_depth, min, TYPE_INT)

    def setMaxHierarchyDepth(self, max):
        self.addResult(self.key_max_depth, max, TYPE_INT)

    def setAll(self, amount_hierarchies, amount_subclasses, average, median, min, max):
        self.addResult(self.key_amount_hierarchies, amount_hierarchies, TYPE_INT)
        self.addResult(self.key_amount_subclasses, amount_subclasses, TYPE_INT)
        self.addResult(self.key_average_depth, average, TYPE_FLOAT)
        self.addResult(self.key_median_depth, median, TYPE_FLOAT)
        self.addResult(self.key_min_depth, min, TYPE_INT)
        self.addResult(self.key_max_depth, max, TYPE_INT)