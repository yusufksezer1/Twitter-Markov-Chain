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
