import enum

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
    SUBORDINATOR        = 16
    QUESTION            = 17
    SIMPLE_QUESTION     = 20
    QUESTION_MARK       = 18
    IMPARATIVE_SENTENCE = 19
    QUESTION_VERB       = 21

TERMINALS = {
        Var.PRONOUN             : ["I", "you", "he", "she", "it", "they", "we"],
        Var.NOUN                : ["bed", "cookie", "boy", "girl", "sun", "sky", "lollipop", "car",
                                   "dog", "cat", "hummus", "computer", "coffee", "programmer",
                                   "firefighter", "policeman", "lawyer", "junkie", "old man",
                                   "designer", "robot", "iRobot", "tree", "fire", "rabbit", "lizard",
                                   "system", "chair", "table", "fly", "flee", "bee", "horse", "donkey",
                                   "pig", "flower", "river", "building", "city", "town", "arab",
                                   "jew", "russian", "terrorist", "suspect"],
        Var.TRANSITIVE_VERB     : ["eat", "make", "want", "is", "kiss", "call", "touch", "develop",
                                   "watch", "drown", "drive", "turn on", "turn off", "kill", "like",
                                   "love", "observe", "hear", "smell", "taste", "learn", "suspect", "close"],
        Var.INTRANSITIVE_VERB   : ["walk", "swim", "play", "sleep", "fly", "cry", "die", "try",
                                   "listen", "learn", "suspect", "run"],
        Var.ADJECTIVE           : ["red", "blue", "yellow", "dark", "light", "big", "small", "fat",
                                   "thin", "greceful", "nerdy", "cool", "sour", "sweet", "hot",
                                   "spicy", "ugly", "pretty", "good", "bad", "short", "long", "tall",
                                   "old", "young", "far", "close", "poor"],
        Var.ARTICLE             : ["a", "the"],
        Var.CONJUNCTION         : ["and", "but", "while", "therefore", "because", "hence",
                                   "as a result", "despite that", "after", "before", "as soon as",
                                   "even though", "so that", "then"],
        Var.ADVERB              : ["freely", "joyfully", "nicely", "hardly", "barely", "perfectly",
                                   "fastly", "slowly", "sadly", "uncontrollably", "far", "close",
                                   "poorly", "restlessly"],
        Var.SUBORDINATOR        : ["that", "who", "which"], #TODO: Currently not used
        Var.COMMA               : [",", ";"],
        Var.QUESTION_MARK       : ["?"],
        Var.QUESTION_VERB       : ["does"],
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

def load_cfg():
    pass

def is_terminal(var):
    return var in TERMINALS.keys()

