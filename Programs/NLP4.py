def pluralize(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"

words = ["cat", "bus", "box", "baby", "church", "toy"]

print("Singular -> Plural")
for word in words:
    print(word, "->", pluralize(word))

Output:
Singular -> Plural
cat -> cats
bus -> buses
box -> boxes
baby -> babies
church -> churches
toy -> toys


