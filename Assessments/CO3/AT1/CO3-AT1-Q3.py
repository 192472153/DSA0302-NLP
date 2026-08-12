from collections import Counter
import math

train = "the student is reading a book the student is learning python"
test = "the student is reading a book"

words = train.split()
test_words = test.split()

uni = Counter(words)
bi = Counter(zip(words, words[1:]))

total = len(words)


# Calculate entropy
def entropy():

    h = 0
    count = 0

    for i in range(1, len(test_words)):

        w1 = test_words[i-1]
        w2 = test_words[i]

        if bi[(w1, w2)] > 0:

            p = bi[(w1, w2)] / uni[w1]

            h = h - math.log2(p)
            count += 1

    return h / count


print("Bigram Entropy =", round(entropy(), 3))

if entropy() < 1:
    print("Low Entropy - More Predictable")
else:
    print("High Entropy - Less Predictable")
