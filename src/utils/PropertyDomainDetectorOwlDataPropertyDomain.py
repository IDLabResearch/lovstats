
from PropertyDomainDetector import PropertyDomainDetector

class PropertyDomainDetectorOwlDataPropertyDomain(PropertyDomainDetector):
    """
    This class implements the detection of the owl:DataPropertyDomain Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyDomainDetectorOwlDataPropertyDomain, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#DataPropertyDomain':
            self.amount += 1

    def getName(self):
        return "propertyDomainDetectorOwlDataPropertyDomain"

    def getVersion(self):
        return "propertyDomainLODStatsDetectorOwlDataPropertyDomain-v1"

    def compute(self):
        self.setAmountDomainProperties(self.amount)


