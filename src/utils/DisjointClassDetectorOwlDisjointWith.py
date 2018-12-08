
from DisjointClassDetector import DisjointClassDetector
from SimplePropertyStats import SimplePropertyStats

class DisjointClassDetectorOwlDisjointWith(DisjointClassDetector):
    """
    This class implements the detection of the owl:disjointWith Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(DisjointClassDetectorOwlDisjointWith, self).__init__()
        self.propertyStats = SimplePropertyStats()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#disjointWith':
            self.propertyStats.count(s, o)

    def getName(self):
        return "disjointClassesDetectorOwlDisjointWith"

    def getVersion(self):
        return "disjointClassesLODStatsDetectorOwlDisjointWith-v1"

    def compute(self):
        self.propertyStats.compute()

        self.setAmountDisjointClasses(self.propertyStats.getAmount())
        #self.setAll(amount=self.propertyStats.getAverage(),
        #            average=self.propertyStats.getAverage(),
        #            median=self.propertyStats.getMedian(),
        #            min=self.propertyStats.getMin(),
        #            max=self.propertyStats.getMax())

