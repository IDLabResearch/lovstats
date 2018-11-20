
from RestrictionTypeDetector import RestrictionTypeDetector
from RestrictionTypeDetector import TYPE_INT

class PropertyDomainDetector(RestrictionTypeDetector):
    """
    This class serves as interface for all Restriction Type Statistics of domain expressions.
    It defines the statistical metric amount.

    Subclasses of this class, should implement the compute method in which they should perform
    their computation and call the set* methods of this class here.
    """
    def __init__(self):
        super(PropertyDomainDetector, self).__init__()
        self.addResult("amount", 0, TYPE_INT)

    def setAmountDomainProperties(self, amount):
        self.addResult("amount", amount, TYPE_INT)
