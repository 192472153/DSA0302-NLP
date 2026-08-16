import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Download required packages
nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),   # words ending with ing
    (r'.*ed$', 'VBD'),    # words ending with ed
    (r'.*ly$', 'RB'),     # words ending with ly
    (r'.*s$', 'NNS'),     # words ending with s
    (r'.*', 'NN')         # default noun
]

tagger = RegexpTagger(patterns)

text = "The boys are playing happily"

words = word_tokenize(text)

tags = tagger.tag(words)

print("POS Tags:")
print(tags)
