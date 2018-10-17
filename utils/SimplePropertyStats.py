from numpy import median

class SimplePropertyStats():
    """dfa"""
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
        self.avg = sum(propertiesLengths) / float(len(propertiesLengths))
        self.median = median(propertiesLengths)

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