class Cve_Feature_Vector:

    def __init__(self, vec):
        self.vector = vec

    def getFeatures(self):
        # returns a dict containing the vector
        return self.vector
    
    def getCsvLine(self):
        # returns the vector as a line which can be written into a CSV file

        mapped_values = list(map(lambda feature: str(feature), self.vector.values()))

        return ','.join(mapped_values)

