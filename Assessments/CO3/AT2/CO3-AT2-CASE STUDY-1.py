import math

print("CASE STUDY 1: SMART MOBILE KEYBOARD PREDICTION SYSTEM")

# 1. Bigram MLE Probability
data_count = 3
data_science_count = 3

bigram_probability = data_science_count / data_count

print("\n1. Bigram MLE")
print("P(science | data) =", bigram_probability)


# 2. Backoff Model
print("\n2. Backoff Model")

bigram = {
    ("data", "science"): 1.0,
    ("science", "is"): 0.66,
    ("science", "drives"): 0.33
}

unigram = {
    "improves": 0.05
}

word1 = "science"
word2 = "improves"

if (word1, word2) in bigram:
    probability = bigram[(word1, word2)]
    print("Using Bigram Model")
else:
    probability = unigram.get(word2, 0.01)
    print("Bigram not found")
    print("Using Unigram Backoff")

print("Probability =", probability)


# 3. Deleted Interpolation
print("\n3. Deleted Interpolation")

lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

trigram_prob = 2 / 3
bigram_prob = 2 / 3
unigram_prob = 2 / 12

interpolation_probability = (
    lambda1 * trigram_prob +
    lambda2 * bigram_prob +
    lambda3 * unigram_prob
)

print("P(data science is) =",
      round(interpolation_probability, 3))


# 4. Entropy Calculation
print("\n4. Entropy Calculation")

p_is = 0.66
p_drives = 0.33

entropy = -(
    p_is * math.log2(p_is) +
    p_drives * math.log2(p_drives)
)

print("Entropy =", round(entropy, 3), "bits")
