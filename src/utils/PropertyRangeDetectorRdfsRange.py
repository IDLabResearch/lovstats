
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
        return "RdfsRange"

    def getVersion(self):
        return "RdfsRange-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountDomainProperties(self.amount)


