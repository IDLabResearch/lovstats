
from ValueTypeClassDetector import ValueTypeClassDetector

class ValueTypeClassDetectorSHACLClass(ValueTypeClassDetector):
    """
    This class implements the detection of the value constraint sh:class.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueTypeClassDetectorSHACLClass, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#class':
            self.number += 1

    def getName(self):
        return "valueTypeClassSHACLClass"

    def getVersion(self):
        return "valueTypeClassLODStatsDetectorSHACLClass-v1"

    def compute(self):
        self.setNumberValueTypeClass(self.number)


