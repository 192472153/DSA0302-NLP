from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

words = [
    "playing",
    "played",
    "player",
    "running",
    "runner",
    "studies",
    "studying",
    "connected",
    "connection",
    "easily"
]

print("Original Word -> Stemmed Word")

for word in words:
    print(word, "->", ps.stem(word))
Output:
Original Word -> Stemmed Word
playing -> play
played -> play
player -> player
running -> run
runner -> runner
studies -> studi
studying -> studi
connected -> connect
connection -> connect
easily -> easili

