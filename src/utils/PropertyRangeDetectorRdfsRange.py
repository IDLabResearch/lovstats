
from PropertyRangeDetector import PropertyRangeDetector

class PropertyRangeDetectorRdfsRange(PropertyRangeDetector):
    """
    This class implements the detection of the rdfs:range Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyRangeDetectorRdfsRange, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2000/01/rdf-schema#range':
            self.amount += 1

    def getName(self):
        return "propertyRangeDetectorRdfsRange"

    def getVersion(self):
        return "propertyRangeLODStatsDetectorRdfsRange-v1"

    def compute(self):
        self.setAmountDomainProperties(self.amount)


