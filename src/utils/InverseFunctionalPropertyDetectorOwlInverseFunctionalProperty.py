
from InverseFunctionalPropertyDetector import InverseFunctionalPropertyDetector

class InverseFunctionalPropertyDetectorOwlInverseFunctionalProperty(InverseFunctionalPropertyDetector):
    """
    This class implements the detection of the owl:InverseFunctionalProperty Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(InverseFunctionalPropertyDetectorOwlInverseFunctionalProperty, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' and \
            o == 'http://www.w3.org/2002/07/owl#InverseFunctionalProperty':
            self.amount += 1

    def getName(self):
        return "OwlInverseFunctionalProperty"

    def getVersion(self):
        return "OwlInverseFunctionalProperty-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountFunctionalProperties(self.amount)


