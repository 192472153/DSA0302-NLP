import nltk

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
sentence = "The intelligent student reads a book"

# Tokenization
words = nltk.word_tokenize(sentence)

# POS tagging
tags = nltk.pos_tag(words)

# Grammar for noun phrase
grammar = "NP: {<DT>?<JJ>*<NN>}"

# Create parser
parser = nltk.RegexpParser(grammar)

# Extract noun phrases
tree = parser.parse(tags)

print("Noun Phrases:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        phrase = " ".join(word for word, tag in subtree.leaves())
        print(phrase)
