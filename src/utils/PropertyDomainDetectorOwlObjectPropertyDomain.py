
from PropertyDomainDetector import PropertyDomainDetector

class PropertyDomainDetectorOwlObjectPropertyDomain(PropertyDomainDetector):
    """
    This class implements the detection of the owl:ObjectPropertyDomain Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyDomainDetectorOwlObjectPropertyDomain, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#ObjectPropertyDomain':
            self.amount += 1

    def getName(self):
        return "propertyDomainDetectorOwlObjectPropertyDomain"

    def getVersion(self):
        return "propertyDomainLODStatsDetectorOwlObjectPropertyDomain-v1"

    def compute(self):
        self.setAmountDomainProperties(self.amount)


