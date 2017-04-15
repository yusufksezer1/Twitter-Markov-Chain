import suffix
import prefix
from immdict import ImmDict
from functools import *

NONWORD = "\n"

def line_gen(fileName):
    with open(fileName, encoding='utf-8') as file:
        yield file.read()

def pairs_gen(fileName, lineGenerator):
    generator = lineGenerator(fileName)
    currPrefix = prefix.new_prefix(NONWORD, NONWORD)
    for line in generator:
        words = line.split()
        for word in words:
            yield (currPrefix, word)
            currPrefix = prefix.shift_in(currPrefix, word)
    yield (currPrefix, NONWORD)

def add_to_chain(chain, pair):
    return chain.put(pair[0], suffix.add_word(chain.get(pair[0]), pair[1]))

def build_chain(add_prefix, generator, imm_dict):
    return reduce(lambda x, y: add_to_chain(x, y), generator, imm_dict)

def build(filename):
    return build_chain(None, pairs_gen(filename, line_gen), ImmDict())

#for pair in pairs_gen('iliad.txt', line_gen):
#    print(pair)

#t = ImmDict()
#suff1 = ImmDict()
#suff1.dictionary = {"great": 2, "silly": 1}
#suff2 = ImmDict()
#suff2.dictionary = {"funny": 8, "nonsense": 1}
#t.dictionary = {("Yusuf", "is"): suff1, ("Navin", "is"): suff2}
#result = add_to_chain(t, (("Yusuf", "is"), "asdffg")).dictionary
#print(result.get(("Yusuf", "is")).dictionary)
#f = ImmDict()
#suff3 = ImmDict()
#suff3.dictionary = {"great": 2, "silly": 1}
#suff4 = ImmDict()
#suff4.dictionary = {"funny": 8, "nonsense": 1}
#f.dictionary = {("Yusuf", "is"): suff3, ("Navin", "is"): suff4}
#result2 = add_to_chain(f, (("Yusuf", "not"), "asdffg")).dictionary
#print(result2.get(("Yusuf", "not")).dictionary)
#print(result)
#result = add_to_chain(t, (("Yusuf", "is"), "silly")).dictionary
#print(result.get(("Yusuf", "is")).dictionary)
#print(result)
#result = pairs_gen('dracula.txt', line_gen)
#for line in result:
#    print(line)

#generator = pairs_gen('test.txt', line_gen)
#chain = build_chain(None, generator, ImmDict())
#for key in chain.dictionary:
#    print(key)
#    print(chain.dictionary[key].dictionary)
#result = build("aladdin.txt")
#for key in result.dictionary:
#    print(key)
#    print(result.dictionary[key].dictionary)

#TESTING
#for line in line_gen('iliad.txt'):
    #print(line)

#for pair in pairs_gen('iliad.txt', line_gen):
    #print(pair)