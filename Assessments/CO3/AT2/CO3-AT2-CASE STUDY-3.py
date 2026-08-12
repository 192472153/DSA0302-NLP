import math

print("CASE STUDY 3: NEWS ANALYTICS AND POS TAG CORRECTION")

# 1. Initial POS Tags
print("\n1. Transformation-Based Tag Correction")

words = ["economic", "growth", "increases", "employment"]

tags = ["JJ", "NN", "NNS", "NN"]

print("\nInitial POS Tags:")

for word, tag in zip(words, tags):
    print(word, "/", tag)


# Transformation Rule
# Change NNS to VBZ if previous tag is NN

for i in range(1, len(tags)):
    if tags[i] == "NNS" and tags[i - 1] == "NN":
        tags[i] = "VBZ"

print("\nCorrected POS Tags:")

for word, tag in zip(words, tags):
    print(word, "/", tag)


# 2. Corrected Sentence
print("\n2. Corrected Sentence")

corrected_sentence = []

for word, tag in zip(words, tags):
    corrected_sentence.append(word + "/" + tag)

print(" ".join(corrected_sentence))


# 3. Word Frequency Distribution
print("\n3. Word Frequency Distribution")

frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

for word, count in frequency.items():
    probability = count / total

    print(word,
          "| Frequency =", count,
          "| Probability =", round(probability, 3))


# 4. Entropy Before and After Correction
print("\n4. Entropy Analysis")

p_nns_before = 0.45
p_vbz_before = 0.55

entropy_before = -(
    p_nns_before * math.log2(p_nns_before) +
    p_vbz_before * math.log2(p_vbz_before)
)

p_nns_after = 0.10
p_vbz_after = 0.90

entropy_after = -(
    p_nns_after * math.log2(p_nns_after) +
    p_vbz_after * math.log2(p_vbz_after)
)

print("Entropy Before Correction =",
      round(entropy_before, 3))

print("Entropy After Correction =",
      round(entropy_after, 3))
