
from ValueTypeDatatypeDetector import ValueTypeDatatypeDetector

class ValueTypeDatatypeDetectorSHACLDatatype(ValueTypeDatatypeDetector):
    """
    This class implements the detection of the value constraint sh:datatype.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(ValueTypeDatatypeDetectorSHACLDatatype, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#datatype':
            self.number += 1

    def getName(self):
        return "valueTypeDatatypeSHACLDatatype"

    def getVersion(self):
        return "valueTypeDatatypeLODStatsDetectorSHACLDatatype-v1"

    def compute(self):
        self.setNumberValueTypeDatatype(self.number)


