
from utils.DisjointPropertyDetector import DisjointPropertyDetector
from SimplePropertyStats import SimplePropertyStats

class DisjointPropertyDetectorOwlDisjointWith(DisjointPropertyDetector):
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
        return "disjointPropertiesDetectorOwlDisjointWith"

    def getVersion(self):
        return "disjointPropertiesLODStatsDetectorOwlDisjointWith-v1"

    def compute(self):
        self.propertyStats.compute()

        self.setAmountDisjointProperties(self.propertyStats.getAmount())
        #self.setAll(amount=self.propertyStats.getAverage(),
        #            average=self.propertyStats.getAverage(),
        #            median=self.propertyStats.getMedian(),
        #            min=self.propertyStats.getMin(),
        #            max=self.propertyStats.getMax())

