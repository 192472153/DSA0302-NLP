words = ["govern", "government", "governance"]

print("Original\tRoot\tAffix\tHierarchy\tNormalized")

for word in words:

    root = "govern"

    if word == "govern":
        affix = "-"
        level = "Base"

    elif word == "government":
        affix = "-ment"
        level = "Level 1"

    elif word == "governance":
        affix = "-ance"
        level = "Level 1"

    print(word,"\t",root,"\t",affix,"\t",level,"\t",root)
