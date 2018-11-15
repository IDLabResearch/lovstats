

TYPE_INT="int"
TYPE_FLOAT="float"
TYPE_BOOLEAN="boolean"

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
            "implementation": self.getImplementation(),
            "results": self.results
        }
        return results

    def getVersion(self):
        raise NotImplementedError

    def getImplementation(self):
        raise NotImplementedError

    def addResult(self, name, value, type):

        if type not in allowed_types:
            raise TypeError("Result type must be one of the following " + str(allowed_types))

        self.results[name] = {
            "value": value,
            "type": type
        }
