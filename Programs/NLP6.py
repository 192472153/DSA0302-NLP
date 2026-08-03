import random

text = "I love python because python is easy and python is powerful"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigrams:
        bigrams[word] = []

    bigrams[word].append(next_word)

current = "I"
result = [current]

for i in range(9):
    if current in bigrams:
        current = random.choice(bigrams[current])
        result.append(current)
    else:
        break

print("Generated Text:")
print(" ".join(result))
