words = ["activate", "activation", "reactivation"]

print("Original\tPrefix\tRoot\tSuffix\tSequence\t\tNormalized")

for word in words:

    prefix = "-"
    suffix = "-"
    root = "activate"

    if word == "activate":
        sequence = "Base"

    elif word == "activation":
        suffix = "-ion"
        sequence = "activate + ion"

    elif word == "reactivation":
        prefix = "re-"
        suffix = "-ion"
        sequence = "re + activate + ion"

    print(word,"\t",prefix,"\t",root,"\t",suffix,"\t",sequence,"\t",root)
