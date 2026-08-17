import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

# Define grammar
grammar = CFG.fromstring("""
S -> VP
VP -> V NP
VP -> V NP PP
NP -> DET N
NP -> DET N PP
PP -> P NP

V -> 'Book'
DET -> 'a'
N -> 'flight' | 'Delhi' | 'window' | 'seat'
P -> 'to' | 'with'
""")

# Create Earley Parser
parser = EarleyChartParser(grammar)

# Input command
sentence = "Book a flight to Delhi with a window seat"

# Simplified input
words = "Book a flight to Delhi with a seat".split()

print("Input:", sentence)
print("\nParse Tree:\n")

# Display parse tree
for tree in parser.parse(words):
    print(tree)
