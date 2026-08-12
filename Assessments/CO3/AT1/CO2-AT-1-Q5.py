# Porter Stemmer (Simple Rule-Based Simulation)

words = ["relational", "relation", "relate"]

print("-" * 100)
print("{:<15}{:<25}{:<20}{:<15}".format(
    "Word", "Applied Rule", "Intermediate", "Final Stem"))
print("-" * 100)

for word in words:

    if word == "relational":
        rule = "remove 'ational'"
        intermediate = "relate"
        stem = "relat"

    elif word == "relation":
        rule = "remove 'ion'"
        intermediate = "relat"
        stem = "relat"

    elif word == "relate":
        rule = "remove 'e'"
        intermediate = "relat"
        stem = "relat"

    print("{:<15}{:<25}{:<20}{:<15}".format(
        word, rule, intermediate, stem))
