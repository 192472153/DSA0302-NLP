import re

text = "John went to the shop. He bought a book."

# Simple reference resolution
text = re.sub(r'\bHe\b', 'John', text)

print("Original Text:")
print("John went to the shop. He bought a book.")

print("\nResolved Text:")
print(text)
