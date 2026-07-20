def fsa(string):
    if string.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"

s = input("Enter a string: ")
print(fsa(s))

Output:
Enter a string: aab
Accepted
