from collections import Counter

# Training data
data = [
    ("the", "DT"),
    ("student", "NN"),
    ("is", "VB"),
    ("reading", "VBG"),
    ("a", "DT"),
    ("book", "NN"),
    ("he", "PRP"),
    ("likes", "VB"),
    ("python", "NN")
]

# Dictionary
tags = dict(data)

def rule_based(words):

    result = []

    for w in words:

        if w in tags:
            tag = tags[w]

        elif w.endswith("ing"):
            tag = "VBG"

        elif w.endswith("ly"):
            tag = "RB"

        elif w.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        result.append((w, tag))

    return result

def stochastic(words):

    result = []

    for w in words:

        if w in tags:
            result.append((w, tags[w]))
        else:
            result.append((w, "NN"))

    return result

def transformation(words):

    result = rule_based(words)

    for i in range(1, len(result)):

        word, tag = result[i]
        previous_word, previous_tag = result[i-1]

        # Rule:
        # word after "is" ending with ing = verb
        if previous_word == "is" and word.endswith("ing"):
            result[i] = (word, "VBG")

    return result

sentence = input("Enter sentence: ")

words = sentence.lower().split()

print("\nRule-Based:")
print(rule_based(words))

print("\nStochastic:")
print(stochastic(words))

print("\nTransformation-Based:")
print(transformation(words))
