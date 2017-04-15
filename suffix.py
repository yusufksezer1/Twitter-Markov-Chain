from immdict import ImmDict
from functools import *

def empty_suffix():
    return ImmDict()

def add_word(suffix, word):
    if suffix is None:
        return ImmDict().put(word, 1)
    elif suffix.get(word) != None:
        return suffix.put(word, 1 + suffix.get(word))
    else:
        return suffix.put(word, 1)

#LOOK AT THIS AGAIN!!!!!
def choose_word(chain, prefix, randomizer):
    suffix = chain.get(prefix)
    totalCount = reduce(lambda x, y: x + y, [suffix.get(key) for key in suffix.dictionary])
    randomNum = randomizer(totalCount)
    probabilityList = [y for lst in [listify(key, suffix.get(key)) for key in suffix.dictionary] for y in lst]
    return probabilityList[randomNum-1]

def listify(key, count):
    if count == 0:
        return []
    if count > 0:
        return [key] + listify(key, count - 1)


#t = {("there", "is"): {"Yusuf": 1, "Panav": 50, "Noah": 1}}
#print(choose_word(t, ("there", "is"), randomizer))
#t = {"Yusuf": 5, "Panav": 3, "Noah": 8}
#probabilityList = [listify(key, t[key]) for key in t]
#print(probabilityList)

#immDict = ImmDict()
#immDict.dictionary = {"Yusuf": 5, "Panav": 3, "Noah": 8}
#print(add_word(None, "Yusuf").dictionary)
#print(add_word(immDict, "Yusuf").dictionary)
#print(add_word(immDict, "Michael").dictionary)