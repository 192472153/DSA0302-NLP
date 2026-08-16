import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
NP -> 'Mary'
VP -> V NP
V -> 'likes'
""")

parser = EarleyChartParser(grammar)

sentence = "John likes Mary".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
