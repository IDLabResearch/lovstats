
from DisjointClassDetector import DisjointClassDetector
from SimplePropertyStats import SimplePropertyStats

class DisjointPropertyDetectorOwlDisjointWith(DisjointClassDetector):
    """
    This class implements the detection of the owl:propertyDisjointWith Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(DisjointPropertyDetectorOwlDisjointWith, self).__init__()
        self.propertyStats = SimplePropertyStats()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#propertyDisjointWith':
            self.propertyStats.count(s, o)

    def getName(self):
        return "OwlClassDisjointWith"

    def getVersion(self):
        return "OwlClassDisjointWith-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.propertyStats.compute()

        self.setAll(amount=self.propertyStats.getAverage(),
                    average=self.propertyStats.getAverage(),
                    median=self.propertyStats.getMedian(),
                    min=self.propertyStats.getMin(),
                    max=self.propertyStats.getMax())

