
from DisjointClassDetector import DisjointClassDetector
from SimplePropertyStats import SimplePropertyStats

class DisjointClassDetectorOwlDisjointWith(DisjointClassDetector):

    def __init__(self):
        super(DisjointClassDetectorOwlDisjointWith, self).__init__()
        self.propertyStats = SimplePropertyStats()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        if p == 'http://www.w3.org/2002/07/owl#disjointWith':
            self.propertyStats.count(s, o)

    def getName(self):
        return "OwlClassDisjointWith"

    def getVersion(self):
        return "OwlClassDisjointWith-v1"

    def getImplementation(self):
        return "LODStatsModule"

    def compute(self):
        self.propertyStats.compute()

        self.setAmountDisjointProperties(self.propertyStats.getAmount())
        self.setAverageDisjoint(self.propertyStats.getAverage())
        self.setMedianDisjoint(self.propertyStats.getMedian())
        self.setMinDisjoint(self.propertyStats.getMin())
        self.setMaxDisjoint(self.propertyStats.getMax())
