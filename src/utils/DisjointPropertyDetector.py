
from RestrictionTypeDetector import RestrictionTypeDetector

class DisjointPropertyDetector(RestrictionTypeDetector):

    def __init__(self):
        super(DisjointPropertyDetector, self).__init__()
        self.amount = 0
        self.average = 0
        self.median = 0
        self.min = 0
        self.max = 0

    def setAmountDisjointProperties(self, amount):
        self.amount = amount

    def setAverageDisjoint(self, average):
        self.average = average

    def setMedianDisjoint(self, median):
        self.median = median

    def setMinDisjoint(self, min):
        self.min = min

    def setMaxDisjoint(self, max):
        self.max = max

    def getResults(self):
        self.compute()

        results = {
            "amount": {
                "value": self.amount,
                "type": "int"
            },
            "average": {
                "value": self.average,
                "type": "float"
            },
            "median": {
                "value": self.median,
                "type": "float"
            },
            "min": {
                "value": self.min,
                "type": "int"
            },
            "max": {
                "value": self.max,
                "type": "int"
            }
        }

        return results