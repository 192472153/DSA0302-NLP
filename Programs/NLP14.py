import nltk
from nltk import CFG

# Define grammar with agreement rules
grammar = CFG.fromstring("""
S -> NP_SG VP_SG | NP_PL VP_PL

NP_SG -> 'boy' | 'girl'
NP_PL -> 'boys' | 'girls'

VP_SG -> 'runs' | 'plays'
VP_PL -> 'run' | 'play'
""")

parser = nltk.ChartParser(grammar)

# Input sentence
sentence = input("Enter a sentence: ").lower().split()

# Check agreement
try:
    trees = list(parser.parse(sentence))

    if trees:
        print("Sentence is grammatically correct.")
    else:
        print("Sentence does not follow agreement rules.")

except ValueError:
    print("Sentence does not follow agreement rules.")
