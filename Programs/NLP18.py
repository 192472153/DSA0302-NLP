import re

# Input logical expression
expression = "Likes(John,Mary)"

# Regular expression pattern
pattern = r"([A-Za-z]+)\(([A-Za-z]+),([A-Za-z]+)\)"

match = re.fullmatch(pattern, expression)

if match:
    predicate = match.group(1)
    argument1 = match.group(2)
    argument2 = match.group(3)

    print("Valid FOPC Expression")
    print("Predicate:", predicate)
    print("Argument 1:", argument1)
    print("Argument 2:", argument2)
else:
    print("Invalid FOPC Expression")
