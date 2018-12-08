
from DisjointPropertyDetector import DisjointPropertyDetector
from utils.ListCreator import ListCreator
from pprint import pprint

class DisjointPropertyDetectorOwlAllDisjointProperties(DisjointPropertyDetector):
    """
        This class implements the detection of owl:AllDisjointProperties Restriction Type Expression.
        For further information have a look at the parent class.
        """

    def __init__(self):
        super(DisjointPropertyDetectorOwlAllDisjointProperties, self).__init__()

        self.disjointPropertiesSubjects = {}
        self.disjoint_properties_list_creator = ListCreator('http://www.w3.org/2002/07/owl#members')

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):
        # Keep track of the (blank) nodes defining a literal pattern
        if o == 'http://www.w3.org/2002/07/owl#AllDisjointProperties':
            self.disjointPropertiesSubjects[s] = o

        # call the list creator which keeps track of all rdf:first and rdf:rest list elements
        self.disjoint_properties_list_creator.count(s, p, o, statement)

    def getName(self):
        return "disjointPropertiesDetectorOwlAllDisjointProperties"

    def getVersion(self):
        return "disjointPropertiesLODStatsDetectorOwlAllDisjointProperties-v1"

    def compute(self):
        self.disjoint_properties_list_creator.compute()

        memberList = self.disjoint_properties_list_creator.get_list()

        # We have now all the owl:members (rdf:first, rdf:rest construct) in memberList
        # additionally we have a list with all AllDisjointProperties subjects
        disjointPropertiesCounter = 0

        for s in self.disjointPropertiesSubjects:
            if s in memberList:
                # Compute the amount of disjoint properties from the pairwise exclusive list
                n = len(memberList[s])
                disjointPropertiesCounter += ((n*n)-n)/2

        self.setAmountDisjointProperties(disjointPropertiesCounter)