def parser(word):

    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse"
    }

    if word in irregular:
        return irregular[word], "Irregular Plural"

    elif word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    elif word.endswith("es"):
        return word[:-2], "Plural Noun"

    elif word.endswith("s"):
        return word[:-1], "Plural Noun"

    else:
        return word, "Singular"


words = ["cars", "boxes", "cities", "children"]

for w in words:
    print(w, "->", parser(w))



