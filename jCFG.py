import enum
import random
import json
from random_word import RandomWords

RETRIES = 5
INVENTORY_SIZE = 750
MIN_CORPUS_COUNT = 1500

DYNAMIC_TERMINALS = {
        "NOUN"        : "noun",
        "TRANSITIVE_VERB"         : "verb",
        "INTRANSITIVE_VERB"       : "verb",
        "ADJECTIVE"   : "adjective",
        "ADVERB"      : "adverb",
}

INVENTORY = {}

TERMINALS = {
        "PRONOUN"             : ["I", "you", "he", "she", "it", "they", "we"],
        "ARTICLE"             : ["a", "the"],
        "CONJUNCTION"         : ["and", "but", "while", "therefore", "because", "hence",
                                   "as a result", "despite that", "after", "before", "as soon as",
                                   "even though", "so that", "then"],
        "COMMA"               : [",", ";"],
        "QUESTION_MARK"       : ["?"],
        "QUESTION_VERB"       : ["does"],
        "NOT_CLAUSE"          : ["does not"],
}

RULES = json.load(open("rules.js", "r"))

INVENTORY = json.load(open("words.js", "r"))
for pos in INVENTORY.keys():
    random.shuffle(INVENTORY[pos])

def is_terminal(var):
    return var in DYNAMIC_TERMINALS.keys()

def random_word(var):
    if var in DYNAMIC_TERMINALS:
        part_of_speech = DYNAMIC_TERMINALS[var]
        return INVENTORY[part_of_speech].pop()
    else:
        assert False, "%d is not a terminal." % var

