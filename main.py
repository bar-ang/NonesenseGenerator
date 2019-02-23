import random
from jCFG import *

NUM_SENTENCES = 20

DEBUG = True

PARSE_TREE = {}

def is_panctuation(word):
    return len(word) == 1 and (ord(word) < ord('a') or ord(word) > ord('z'))

def pretty(sentence):
    #for i, word in enumerate(sentence):
    #    if is_panctuation(word):
    #        sentence[i-1] += word
    #        sentence.pop(i)
    return " ".join(sentence).capitalize() + "."

def jibberish(root=Var.SENTENCE, parse_tree=PARSE_TREE):
    if is_terminal(root):
        choice = [random.choice(TERMINALS[root])]
        parse_tree[root] = choice
        return choice

    sentence = []
    rule = random.choice(RULES[root])
    for var in rule:
        sentence += jibberish(var)

    return sentence

def main(args=None):
    sentences = [pretty(jibberish()) for i in range(NUM_SENTENCES)]
    for i, sen in enumerate(sentences):
        print("(%s) %s" % (i + 1, sen))

if __name__ == "__main__":
    main()

