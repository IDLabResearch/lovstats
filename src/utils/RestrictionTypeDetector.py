
import rdflib
TYPE_INT=rdflib.XSD.integer
TYPE_FLOAT=rdflib.XSD.float
TYPE_BOOLEAN=rdflib.XSD.boolean
MEASURE_OCCURRENCE="restrictionTypeOccurrence"
MEASURE_HIERARCHY_OCCURRENCE="hierarchyOccurrence"
MEASURE_HIERARCHY_MIN_DEPTH="minHierarchyDepth"
MEASURE_HIERARCHY_MAX_DEPTH="maxHierarchyDepth"
MEASURE_HIERARCHY_AVERAGE_DEPTH="averageHierarchyDepth"
MEASURE_HIERARCHY_MEDIAN_DEPTH="medianHierarchyDepth"

allowed_types=[TYPE_INT, TYPE_FLOAT, TYPE_BOOLEAN]

class RestrictionTypeDetector(object):
    """
    This class serves as interface for all Restriction Type Detectors.
    The detector output contains the version-name, the implementation-name and the actual results.
    Specific detetor subclasses have to add the results using the addResult method.
    """

    def __init__(self):
        self.results = {}

    def getName(self):
        raise NotImplementedError

    def getVersion(self):
        raise NotImplementedError

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        raise NotImplementedError

    def compute(self):
        pass

    def getDetectorOutput(self):
        results = {
            "version": self.getVersion(),
            "restriction-type": self.getRestrictionType(),
            "implementation": "lodstatsExtension",
            "results": self.results
        }
        return results

    def getVersion(self):
        raise NotImplementedError

    def getRestrictionType(self):
        raise NotImplementedError

    def addResult(self, name, value, type):

        if type not in allowed_types:
            raise TypeError("Result type must be one of the following " + str(allowed_types))

        self.results[name] = {
            "value": value,
            "type": type
        }
