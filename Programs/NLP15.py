import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define probabilistic grammar
grammar = PCFG.fromstring("""
S -> NP VP [1.0]

NP -> 'John' [0.5] | 'Mary' [0.5]

VP -> V NP [1.0]

V -> 'likes' [0.6] | 'sees' [0.4]
""")

# Create Viterbi parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "John likes Mary".split()

# Parse and display result
for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
