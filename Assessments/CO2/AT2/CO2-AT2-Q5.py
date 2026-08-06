words = ["create", "creates", "creating"]

print("Original\tSuffix\tGrammar\t\t\tRoot\tNormalized")

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"
        root = "create"

    elif word == "creates":
        suffix = "-s"
        grammar = "Third Person Singular"
        root = "create"

    elif word == "creating":
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"

    print(word,"\t",suffix,"\t",grammar,"\t",root,"\t",root)
