# CFG Tree using NLTK
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'book'
V -> 'reads'
""")

sentence = "the boy reads a book".split()

parser = ChartParser(grammar)

print("CFG Parse Tree:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()


# Simple Dependency Parsing Representation
print("\nDependency Relationships:")
print("reads --> boy (Subject)")
print("reads --> book (Object)")
