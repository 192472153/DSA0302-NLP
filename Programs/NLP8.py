pos_prob = {
    "I": {"PRON": 1.0},
    "play": {"VERB": 0.8, "NOUN": 0.2},
    "football": {"NOUN": 1.0},
    "every": {"DET": 1.0},
    "day": {"NOUN": 0.9, "VERB": 0.1}
}

sentence = "I play football every day"

words = sentence.split()

print("POS Tagging:")

for word in words:
    if word in pos_prob:
        tag = max(pos_prob[word], key=pos_prob[word].get)
        print(word, ":", tag)
    else:
        print(word, ": UNKNOWN")
