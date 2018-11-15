
from PropertyDomainDetector import PropertyDomainDetector

class PropertyDomainDetectorRdfsDomain(PropertyDomainDetector):
    """
    This class implements the detection of the owl:FunctionalProperty Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(PropertyDomainDetectorRdfsDomain, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2000/01/rdf-schema#domain':
            self.amount += 1

    def getName(self):
        return "RdfsDomain"

    def getVersion(self):
        return "RdfsDomain-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountDomainProperties(self.amount)


