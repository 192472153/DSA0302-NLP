words = ["analyzing", "analysis", "analytical"]

print("Original\tRoot\tAffix\tType\t\tNormalized")

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        mtype = "Inflectional"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        mtype = "Derivational"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        mtype = "Derivational"

    print(word,"\t",root,"\t",affix,"\t",mtype,"\t",root)
