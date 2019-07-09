
from SubsumptionDetector import SubsumptionDetector
from numpy import median
from utils import util_functions

class SubsumptionDetectorOwlSubClassOf(SubsumptionDetector):
    """
    This class implements the detection of the owl:SubClassOf Restriction Type Expression.
    For further information have a look at the parent class.
    """
    def __init__(self):
        super(SubsumptionDetectorOwlSubClassOf, self).__init__()
        self.graph = {}
        self.c = 0
        self.amountSubClasses = 0
        self.roots = set()
        self.subjectsWithManualIRIDeclaration = set()
        self.potentialSubClasses = {}
        self.potentialSuperClasses = set()

    def count(self, s, p, o, s_blank, o_l, o_blank, statement):

        # wee need to keep track of all blank nodes which manually get an IRI assigned
        if p == 'http://www.w3.org/2002/07/owl#IRI':
            self.subjectsWithManualIRIDeclaration.add(s)

        if p == 'http://www.w3.org/2002/07/owl#SubClassOf':
            if statement.object.is_resource():
                self.amountSubClasses += 1
            else:
                # it is a blank node, but still it could be assigned an IRI with owl:IRI later or before in the stream
                self.potentialSuperClasses.add(o)
                if o in self.potentialSubClasses:
                    self.potentialSubClasses[o].append(s)
                else:
                    self.potentialSubClasses[o] = [s]

            # Keep track of potential roots
            self.roots.add(o)
            # remove every subclass from potential roots
            if s in self.roots:
                self.roots.remove(s)
            if o in self.graph:
                self.graph[o].append(s)
            else:
                self.graph[o] = [s]
            self.c += 1

    def getName(self):
        return "subsumptionDetectorOwlSubClassOf"

    def getVersion(self):
        return "subsumptionLODStatsDetectorOwlSubClassOf-v1"

    def compute(self):

        hierarchies_depths = util_functions.compute_depths(self.graph, self.roots)

        if hierarchies_depths:
            average_depth=sum(hierarchies_depths) / float(len(hierarchies_depths))
        else:
            average_depth=0

        # all potential superclasses which have a manual owl:IRI declaration are real super classes
        superClasses = self.subjectsWithManualIRIDeclaration.intersection(self.potentialSuperClasses)

        # one superclass can have multiple subclasses, get the number of subclasses for each potential superclass
        # which is a superclass
        for sc in self.potentialSubClasses:
            if sc in superClasses:
                self.amountSubClasses += len(self.potentialSubClasses[sc])

        self.setAmountSubclasses(self.amountSubClasses);

        # We are not considering other measures than occurrence in the current version
        #self.setAll(amount_hierarchies=len(hierarchies_depths),
        #            amount_subclasses=self.c,
        #            average=average_depth,
        #            median=median(hierarchies_depths) if hierarchies_depths else 0,
        #            min=min(hierarchies_depths) if hierarchies_depths else 0,
        #            max=max(hierarchies_depths) if hierarchies_depths else 0)


