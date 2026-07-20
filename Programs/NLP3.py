import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "studies", "running", "connected"]

for word in words:
    print(word, "->", ps.stem(word))

Output:
playing -> play
studies -> studi
running -> run
connected -> connect
