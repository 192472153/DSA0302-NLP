from collections import Counter

text = """
the student is reading
the student is learning
the teacher is reading
the teacher is teaching
the student likes python
"""

words = text.lower().split()

uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))

total = len(words)


# Unigram probability
def P1(w):
    return uni[w] / total


# Bigram probability
def P2(w1, w2):
    if uni[w1] == 0:
        return 0
    return bi[(w1, w2)] / uni[w1]


# Trigram probability
def P3(w1, w2, w3):
    if bi[(w1, w2)] == 0:
        return 0
    return tri[(w1, w2, w3)] / bi[(w1, w2)]


# Backoff
def backoff(w1, w2, w):
    p = P3(w1, w2, w)

    if p > 0:
        return p

    p = P2(w2, w)

    if p > 0:
        return p

    return P1(w)


# Interpolation
def interpolation(w1, w2, w):
    return (
        0.2 * P1(w)
        + 0.3 * P2(w2, w)
        + 0.5 * P3(w1, w2, w)
    )


# Prediction
sentence = input("Enter sentence: ")
w = sentence.lower().split()

w1 = w[-2]
w2 = w[-1]

print("\nTop predictions:")

result = []

for word in uni:
    p = backoff(w1, w2, word)
    result.append((word, p))

result.sort(key=lambda x: x[1], reverse=True)

for word, p in result[:5]:
    print(word, round(p, 3))

print("\nDeleted Interpolation:")

result = []

for word in uni:
    p = interpolation(w1, w2, word)
    result.append((word, p))

result.sort(key=lambda x: x[1], reverse=True)

for word, p in result[:5]:
    print(word, round(p, 3))
