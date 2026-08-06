words = ["disagree", "agreement", "agreeable"]

print("Word\t\tPrefix\tRoot\tSuffix\tType\t\tMeaning")

for word in words:

    prefix = "-"
    suffix = "-"
    root = "agree"

    if word == "disagree":
        prefix = "dis-"
        mtype = "Derivational"
        meaning = "Negative"

    elif word == "agreement":
        suffix = "-ment"
        mtype = "Derivational"
        meaning = "State or Result"

    elif word == "agreeable":
        suffix = "-able"
        mtype = "Derivational"
        meaning = "Capability"

    print(word,"\t",prefix,"\t",root,"\t",suffix,"\t",mtype,"\t",meaning)

print("\nNormalized Form : agree")
