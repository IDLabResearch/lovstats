
from PropertyRangeDetector import PropertyRangeDetector

class PropertyRangeDetectorOwlDataPropertyRange(PropertyRangeDetector):
    """
    This class implements the detection of the owl:ObjectPropertyRange Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyRangeDetectorOwlDataPropertyRange, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#DataPropertyRange':
            self.amount += 1

    def getName(self):
        return "propertyRangeDetectorOwlDataPropertyRange"

    def getVersion(self):
        return "propertyRangeLODStatsDetectorOwlDataPropertyRange-v1"

    def compute(self):
        self.setAmountRangeProperties(self.amount)


