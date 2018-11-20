
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT

class AsymmetricPropertiesDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of asymmetric properties expressions.
    It defines the statistical metric amount.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(AsymmetricPropertiesDetector, self).__init__()
        self.addResult("amount", 0, TYPE_INT)

    def setAmountAsymmetricProperties(self, amount):
        self.addResult("amount", amount, TYPE_INT)
