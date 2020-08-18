
from OtherIgnoredPropertiesDetector import OtherIgnoredPropertiesDetector

class OtherIgnoredPropertiesDetectorSHACLIgnoredProperties(OtherIgnoredPropertiesDetector):
    """
    This class implements the detection of the ignored properties for 'closed' shapes constraint sh:ignoredProperties.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(OtherIgnoredPropertiesDetectorSHACLIgnoredProperties, self).__init__()
        self.number = 0

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/ns/shacl#ignoredProperties':
            self.number += 1

    def getName(self):
        return "otherIgnoredPropertiesLODStatsDetectorSHACLIgnoredProperties"

    def getVersion(self):
        return "otherIgnoredPropertiesLODStatsDetectorSHACLIgnoredProperties-v1"

    def compute(self):
        self.setNumberOtherIgnoredProperties(self.number)


