import re

products = [
    "Apple iPhone",
    "Apple Watch",
    "Samsung Galaxy",
    "Galaxy Buds",
    "Redmi Note",
    "Dell Laptop",
    "HP Laptop",
    "Wireless Mouse",
    "Gaming Keyboard"
]

# Search Keyword
keyword = input("Enter Search Keyword: ")

print("\nExact Match")
exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]
print(exact)

print("\nPrefix Match")
prefix = [p for p in products if re.match(keyword, p, re.IGNORECASE)]
print(prefix)

print("\nSuffix Match")
suffix = [p for p in products if re.search(keyword + r"$", p, re.IGNORECASE)]
print(suffix)

print("\nPartial Match")
partial = [p for p in products if re.search(keyword, p, re.IGNORECASE)]
print(partial)

print("\nCase-Insensitive Match")
case = [p for p in products if re.search(keyword, p, re.IGNORECASE)]
print(case)

print("\n----- Report -----")
print("Exact Matches :", len(exact))
print("Prefix Matches :", len(prefix))
print("Suffix Matches :", len(suffix))
print("Partial Matches :", len(partial))
print("Case-Insensitive Matches :", len(case))
