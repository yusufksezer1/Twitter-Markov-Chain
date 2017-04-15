class ImmDict:

    def __init__(self):
        self.dictionary = {}

    #revisit this method
    def put(self, k, v):
        newImmDict = ImmDict()
        newImmDict.dictionary = {**self.dictionary, **{k:v}}
        return newImmDict

    def get(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        return None

    def keys(self):
        return list(self.dictionary.keys())

    def values(self):
        return list(self.dictionary.values())