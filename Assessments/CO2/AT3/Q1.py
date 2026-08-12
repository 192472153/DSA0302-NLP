from nltk.stem import PorterStemmer
import re

text = """
Infection is common in infectious diseases.
The patient was infected with bacteria.
Doctors study infection and infectious conditions.
"""

# Preprocessing
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# Porter Stemmer
ps = PorterStemmer()

print("Original -> Stemmed")
for word in words:
    print(word, "->", ps.stem(word))
