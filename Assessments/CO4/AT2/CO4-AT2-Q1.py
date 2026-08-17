import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define CFG grammar
grammar = CFG.fromstring("""
S -> VP
VP -> V PRON NP
NP -> DET N
NP -> DET N PP
NP -> NP PP
PP -> P NP

V -> 'Show'
PRON -> 'me'
DET -> 'the' | 'last'
N -> 'transactions' | 'card' | 'month'
P -> 'with' | 'from'
""")

# Create parser
parser = ChartParser(grammar)

# Input sentence
sentence = "Show me the transactions with the card from last month"

words = sentence.split()

print("Input:", sentence)
print("\nPossible Parse Trees:\n")

# Display parse trees
for tree in parser.parse(words):
    print(tree)
