
from IrreflexiveObjectPropertiesDetector import IrreflexiveObjectPropertiesDetector

class IrreflexiveObjectPropertiesDetectorOwlIrreflexiveProperty(IrreflexiveObjectPropertiesDetector):
    """
    This class implements the detection of the owl:IrreflexiveProperty Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(IrreflexiveObjectPropertiesDetectorOwlIrreflexiveProperty, self).__init__()
        self.amount = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if statement.object.is_resource() and \
                statement.subject.is_resource() and \
                        p == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type' and \
                        o == 'http://www.w3.org/2002/07/owl#IrreflexiveProperty':
            self.amount += 1

    def getName(self):
        return "OwlIrreflexiveProperty"

    def getVersion(self):
        return "OwlIrreflexiveProperty-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.setAmountIrreflexiveProperties(self.amount)


