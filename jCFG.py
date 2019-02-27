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


INVENTORY = {}

TERMINALS = {
        Var.PRONOUN             : ["I", "you", "he", "she", "it", "they", "we"],
        Var.NOUN                : ["bed", "cookie", "boy", "girl", "sun", "sky", "lollipop", "car",
                                   "dog", "cat", "hummus", "computer", "coffee", "programmer",
                                   "firefighter", "policeman", "lawyer", "junkie", "old man",
                                   "designer", "robot", "iRobot", "tree", "fire", "rabbit", "lizard",
                                   "system", "chair", "table", "fly", "flee", "bee", "horse", "donkey",
                                   "pig", "flower", "river", "building", "city", "town", "arab",
                                   "jew", "russian", "terrorist", "suspect", "man", "woman", "nigger",
                                   "gay", "straight", "goat", "giraffe", "truth", "wife", "politician",
                                   "husband", "engineer", "couple", "marrige", "tv", "iphone", "google crome",
                                   "king", "queen", "prince", "princess", "dragon", "fish", "turkey", "virus",
                                   "monkey", "hamburger", "fries", "salad", "ice cream", "ketchup",
                                   "rice", "pasta", "wind", "sea", "ocean"],
        Var.TRANSITIVE_VERB     : ["eat", "make", "want", "is", "kiss", "call", "touch", "develop",
                                   "watch", "drown", "drive", "turn on", "turn off", "kill", "like",
                                   "love", "observe", "hear", "smell", "taste", "learn", "suspect", "close",
                                   "scare", "adore", "throw", "enlarge", "use", "see", "reach", "damage",
                                   "check"],
        Var.INTRANSITIVE_VERB   : ["walk", "swim", "play", "sleep", "fly", "cry", "die", "try",
                                   "listen", "learn", "suspect", "run"],
        Var.ADJECTIVE           : ["red", "blue", "yellow", "dark", "light", "big", "small", "fat",
                                   "thin", "greceful", "nerdy", "cool", "sour", "sweet", "hot",
                                   "spicy", "ugly", "pretty", "good", "bad", "short", "long", "tall",
                                   "old", "young", "far", "close", "poor", "slow", "fast", "shiny", "gay",
                                   "stright", "black", "chinese", "french", "english", "jewish", "muslim",
                                   "buddahist", "american", "german", "japanese", "swedish", "dutch", "natural",
                                   "industrial", "true", "false", "deep", "scary", "terrifying", "adorable",
                                   "precise", "blurry", "fuzzy", "smart", "dumb", "practical",
                                   "theoretical", "abstract", "sharp", "smooth", "dry", "wet", "comfortable",
                                   "jealous", "confident", "inconfident", "2-dimentional", "3-dimentional",],
        Var.ARTICLE             : ["a", "the"],
        Var.CONJUNCTION         : ["and", "but", "while", "therefore", "because", "hence",
                                   "as a result", "despite that", "after", "before", "as soon as",
                                   "even though", "so that", "then"],
        Var.ADVERB              : ["freely", "joyfully", "nicely", "hardly", "barely", "perfectly",
                                   "fastly", "slowly", "sadly", "uncontrollably", "mainly", "peacefully",
                                   "poorly", "restlessly", "generally", "now", "this morning", "tomorrow",
                                   "currently", "today"],
        Var.COMMA               : [",", ";"],
        Var.QUESTION_MARK       : ["?"],
        Var.QUESTION_VERB       : ["does"],
        Var.NOT_CLAUSE          : ["does not"],
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

#for tries in range(RETRIES):
#    try:
#        word_generator = RandomWords()
#    except:
#        pass
#    else:
#        break
#else:
#    word_generator = RandomWords()

#for part_of_speech in DYNAMIC_TERMINALS.values():
#    for tries in range(RETRIES):
#        try:
#            INVENTORY[part_of_speech] = word_generator.get_random_words(includePartOfSpeech=part_of_speech, limit=INVENTORY_SIZE, minCorpusCount=MIN_CORPUS_COUNT)
#        except:
#            pass
#        else:
#            break
#    else:
#        INVENTORY[part_of_speech] = word_generator.get_random_words(includePartOfSpeech=part_of_speech, limit=INVENTORY_SIZE, minCorpusCount=MIN_CORPUS_COUNT)


#print(INVENTORY)

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
