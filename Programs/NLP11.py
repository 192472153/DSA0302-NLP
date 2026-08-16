import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> V NP
V -> 'likes'
NP -> 'Mary'
""")

parser = nltk.ChartParser(grammar)

sentence = "John likes Mary".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
