import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download('wordnet')

word = "bank"

# Get synsets
synsets = wordnet.synsets(word)

print("Synsets and Meanings:")

for synset in synsets:
    print("\nSynset:", synset.name())
    print("Meaning:", synset.definition())
