import re
from collections import Counter
corpus = """
the student is reading a book
the student is writing a program
the student is learning python
the teacher is reading a book
the teacher is teaching python
the student likes python
the student likes machine learning
the teacher likes machine learning
students are learning language processing
students are reading books
python is a programming language
machine learning is interesting
"""
sentences = corpus.lower().strip().split("\n")
tokenized = []
for sentence in sentences:
    words = re.findall(r'\b\w+\b', sentence)
    tokenized.append(["<s>"] + words + ["</s>"])
unigram = Counter()
bigram = Counter()
trigram = Counter()
for words in tokenized:
    for word in words:
        unigram[word] += 1
    for i in range(len(words) - 1):
        bigram[(words[i], words[i + 1])] += 1
    for i in range(len(words) - 2):
        trigram[(words[i], words[i + 1], words[i + 2])] += 1
def unigram_probability(word):
    return unigram[word] / sum(unigram.values())
def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0
    return bigram[(w1, w2)] / unigram[w1]
def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0
    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]
print("UNIGRAM COUNTS")
for word, count in unigram.items():
    print(word, ":", count)

print("\nBIGRAM COUNTS")
for gram, count in bigram.items():
    print(gram, ":", count)

print("\nTRIGRAM COUNTS")
for gram, count in trigram.items():
    print(gram, ":", count)
def predict_next(sentence, n):
    words = re.findall(r'\b\w+\b', sentence.lower())

    candidates = set(unigram.keys())
    predictions = []

    for word in candidates:

        if n == 1:
            probability = unigram_probability(word)

        elif n == 2:
            if len(words) < 1:
                probability = 0
            else:
                probability = bigram_probability(words[-1], word)

        elif n == 3:
            if len(words) < 2:
                probability = 0
            else:
                probability = trigram_probability(
                    words[-2], words[-1], word
                )

        predictions.append((word, probability))

    predictions.sort(key=lambda x: x[1], reverse=True)

    return predictions[:5]


n = int(input("\nEnter N (1, 2 or 3): "))

sentence = input("Enter incomplete sentence: ")

print("\nTop-5 Predictions:")

results = predict_next(sentence, n)

for word, probability in results:
    print(word, "->", round(probability, 4))


print("\nUnseen N-gram demonstration:")

print(
    "Probability of 'student banana' =",
    bigram_probability("student", "banana")
)

print(
    "Probability of 'student is banana' =",
    trigram_probability("student", "is", "banana")
)
