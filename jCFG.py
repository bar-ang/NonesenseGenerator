import enum
import random
import json
from random_word import RandomWords

RETRIES = 5
INVENTORY_SIZE = 750
MIN_CORPUS_COUNT = 1500

class Var(enum.Enum):
    SENTENCE            = 0
    SIMPLE_SENTENCE     = 8
    SUBJECT             = 1
    VERB                = 2
    OBJECT              = 3
    NOUN                = 4
    ARTICLE             = 5
    ADJECTIVE           = 6
    NOUN_PHRASE         = 7
    VERB_PHRASE         = 15
    TRANSITIVE_VERB     = 9
    INTRANSITIVE_VERB   = 10
    CONJUNCTION         = 11
    COMMA               = 12
    PRONOUN             = 13
    ADVERB              = 14
    SUBORDINATOR        = 16 #TODO NOT USED
    QUESTION            = 17
    SIMPLE_QUESTION     = 20
    QUESTION_MARK       = 18
    IMPARATIVE_SENTENCE = 19
    QUESTION_VERB       = 21
    ADJUNCT_PHRASE      = 22
    ADJUNCT             = 23 #TODO NOT USED
    NOT_CLAUSE          = 24


DYNAMIC_TERMINALS = {
        Var.NOUN        : "noun",
        Var.TRANSITIVE_VERB         : "verb",
        Var.INTRANSITIVE_VERB       : "verb",
        Var.ADJECTIVE   : "adjective",
        Var.ADVERB      : "adverb",
}

RULES = {
        Var.SENTENCE : [
            [Var.IMPARATIVE_SENTENCE],
            [Var.IMPARATIVE_SENTENCE],
            [Var.IMPARATIVE_SENTENCE],
            [Var.QUESTION],
        ],

        Var.IMPARATIVE_SENTENCE : [
            [Var.SIMPLE_SENTENCE],
            [Var.SIMPLE_SENTENCE, Var.COMMA, Var.CONJUNCTION, Var.IMPARATIVE_SENTENCE]
        ],

        Var.QUESTION : [
            [Var.SIMPLE_QUESTION, Var.QUESTION_MARK],
        ],

        Var.SIMPLE_QUESTION : [
            [Var.QUESTION_VERB, Var.SUBJECT, Var.VERB_PHRASE],
        ],

        Var.SIMPLE_SENTENCE : [
            [Var.SUBJECT, Var.VERB_PHRASE],
        ],

        Var.VERB_PHRASE : [
            [Var.VERB],
            [Var.NOT_CLAUSE, Var.VERB]
        ],

        Var.VERB : [
            [Var.TRANSITIVE_VERB, Var.OBJECT],
            [Var.INTRANSITIVE_VERB],
            [Var.TRANSITIVE_VERB, Var.OBJECT, Var.ADVERB],
            [Var.INTRANSITIVE_VERB, Var.ADVERB],
            [Var.ADVERB, Var.TRANSITIVE_VERB, Var.OBJECT],
        ],

        Var.SUBJECT : [
            [Var.NOUN_PHRASE],
            [Var.PRONOUN],
        ],

        Var.OBJECT : [
            [Var.NOUN_PHRASE],
        ],

        Var.NOUN_PHRASE : [
            [Var.ARTICLE, Var.NOUN],
            [Var.ARTICLE, Var.ADJECTIVE, Var.NOUN],
        ],
}

INVENTORY = json.load(open("words.js", "r"))
for pos in INVENTORY.keys():
    random.shuffle(INVENTORY[pos])


def load_cfg():
    pass

def is_terminal(var):
    return var in TERMINALS.keys()

def random_word(var):
    if var in DYNAMIC_TERMINALS:
        part_of_speech = DYNAMIC_TERMINALS[var]
        return INVENTORY[part_of_speech].pop()
    elif var in TERMINALS:
        return random.choice(TERMINALS[var])
    else:
        assert False, "%d is not a terminal." % var
