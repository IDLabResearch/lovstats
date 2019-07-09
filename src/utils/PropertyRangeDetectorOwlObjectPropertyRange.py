
from PropertyRangeDetector import PropertyRangeDetector

class PropertyRangeDetectorOwlObjectPropertyRange(PropertyRangeDetector):
    """
    This class implements the detection of the owl:ObjectPropertyRange Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyRangeDetectorOwlObjectPropertyRange, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#ObjectPropertyRange':
            self.amount += 1

    def getName(self):
        return "propertyRangeDetectorOwlObjectPropertyRange"

    def getVersion(self):
        return "propertyRangeLODStatsDetectorOwlObjectPropertyRange-v1"

    def compute(self):
        self.setAmountRangeProperties(self.amount)


