import prefix
import suffix
import builder
import random
from functools import *

punctuation = ['.', '?', '!', ')']

def get_word_list(chain, pre, randomizer, word_count, NONWORD):
    t = suffix.choose_word(chain, pre, randomizer)
    if word_count == 0 or t == NONWORD:
        return tuple()
    else:
        return (suffix.choose_word(chain, pre, randomizer), ) + get_word_list(chain, prefix.shift_in(pre, t), randomizer, word_count - 1, NONWORD)

def generate(chain, randomizer, word_count, NONWORD):
    word_list = get_word_list(chain, ('\n',  '\n'), randomizer, word_count, NONWORD)
    sBuilder = word_list[0].capitalize() + " "
    for i in range(1, len(word_list)):
        sBuilder += word_list[i] + " "
        if any(char.endswith(p) for char in word_list[i] for p in punctuation):
            if word_list[i].__contains__('...'):
                pass
            else:
                break
    return sBuilder
    #return reduce(lambda x, y: x + " " + y, word_list, "")
