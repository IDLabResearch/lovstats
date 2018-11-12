from numpy import median

class SimplePropertyStats():
    """
    This class can be used to collect simple statistics (min/max, avg/median) of properties with multiple objects.
    E.g. given the RDF triples:
        ex:Human  owl:disjointWith ex:Animal .
        ex:Car    owl:disjointWith ex:Plane, ex:Boat, ex:Animal .
        ex:Boat   owl:disjointWith ex:Plane, ex:Car, ex:Animal .

    the min amount of disjointWith is computed (in this example 1), the max (in this example 3), the average and the median.
    """
    def __init__(self):
        self.properties = {}
        self.c = 0
        self.avg = 0
        self.median = 0
        self.min = 0
        self.max  = 0
        self.amount  = 0

    def count(self, s, o):
        if s in self.properties:
            self.properties[s].append(o)
            if len(self.properties[s]) > self.max:
                self.max = len(self.properties[s])
        else:
            self.properties[s] = [o]
        self.c += 1

    def compute(self):
        self.min = self.max
        propertiesLengths = []
        for property in self.properties:
            # find the minimum
            current_length = len(self.properties[property])
            if current_length < self.min:
                self.min = current_length
            propertiesLengths.append(current_length)

        self.amount = self.c

        if(len(propertiesLengths) > 0):
            self.avg = sum(propertiesLengths) / float(len(propertiesLengths))
            self.median = median(propertiesLengths)
        else:
            self.avg = 0
            self.median = 0

    def getAverage(self):
        return self.avg

    def getMedian(self):
        return self.median

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def getAmount(self):
        return self.amount