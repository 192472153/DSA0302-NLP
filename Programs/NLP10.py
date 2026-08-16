sentence = ["I", "am", "playing", "football"]

# Initial tags
tags = [
    ("I", "NN"),
    ("am", "NN"),
    ("playing", "NN"),
    ("football", "NN")
]

# Transformation rules
new_tags = []

for word, tag in tags:

    if word == "I":
        tag = "PRP"

    elif word == "am":
        tag = "VBP"

    elif word.endswith("ing"):
        tag = "VBG"

    new_tags.append((word, tag))

print("Final POS Tags:")
print(new_tags)
