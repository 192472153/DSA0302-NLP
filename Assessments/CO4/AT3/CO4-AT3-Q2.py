from nltk import CFG
from nltk.parse import RecursiveDescentParser
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'I'
VP -> V NP
V -> 'like'
NP -> 'Python'
""")

sentence = "I like Python".split()

# Top-Down Parser
print("Top-Down Parsing:")
top_down_parser = RecursiveDescentParser(grammar)

for tree in top_down_parser.parse(sentence):
    print(tree)


# Earley Parser
print("\nEarley Parsing:")
earley_parser = EarleyChartParser(grammar)

for tree in earley_parser.parse(sentence):
    print(tree)
