import nltk
from nltk.wsd import lesk

# Download required data
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input sentence
sentence = "I went to the bank to deposit money"

# Find the meaning of the word "bank"
sense = lesk(sentence.split(), "bank")

print("Word: bank")

if sense:
    print("Synset:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No meaning found")
