import json
import random
from random_word import RandomWords

FILE = "words.js"

DICT_SIZE = 1500
MIN_CORPUS_COUNT = 300000
MAX_CORPUS_COUNT = None

WORD_TYPES = ["noun", "verb", "adjective", "adverb"]

word_generator = RandomWords()

inventory = {}
for pos in WORD_TYPES:
    if MAX_CORPUS_COUNT is None:
        inventory[pos] = word_generator.get_random_words(includePartOfSpeech=pos, limit=DICT_SIZE,
                                                         minCorpusCount=MIN_CORPUS_COUNT)
    else:
        inventory[pos] = word_generator.get_random_words(includePartOfSpeech=pos, limit=DICT_SIZE,
                                                         minCorpusCount=MIN_CORPUS_COUNT, maxCorpusCount=MAX_CORPUS_COUNT)

jsons = json.dumps(inventory)

f = open(FILE, "w")
f.write(jsons)
f.close()

#print(jsons)
