import nltk
from nltk import CFG

# Define the grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John' | 'Mary'
VP -> V NP
V -> 'likes'
""")

# Create parser
parser = nltk.ChartParser(grammar)

# Input sentence
sentence = "John likes Mary".split()

# Generate parse tree
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
