


class RestrictionTypeDetector(object):

    def __init__(self):
        pass

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
            "results": self.getResults()
        }
        return results

    def getVersion(self):
        raise NotImplementedError

    def getImplementation(self):
        raise NotImplementedError

    def getResults(self):
        raise NotImplementedError