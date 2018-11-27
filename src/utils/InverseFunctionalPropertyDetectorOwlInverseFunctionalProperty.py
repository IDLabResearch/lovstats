
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
        return "inverseFunctionalPropertiesDetectorOwlInverseFunctionalProperty"

    def getVersion(self):
        return "inverseFunctionalPropertiesDetectorOwlInverseFunctionalProperty-v1"

    def compute(self):
        self.setAmountFunctionalProperties(self.amount)


