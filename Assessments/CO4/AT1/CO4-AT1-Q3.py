# Word Sense Disambiguation

queries = {
    "Apple accessories": "iPhone Charger",
    "Mouse wireless": "Bluetooth Mouse",
    "Java tutorial": "Coding Lessons",
    "Python course": "Software Development Training"
}

print("Word Sense Disambiguation:\n")

for query, result in queries.items():
    
    if "Apple" in query:
        sense = "Technology Brand"
    
    elif "Mouse" in query:
        sense = "Computer Device"
    
    elif "Java" in query:
        sense = "Programming Language"
    
    elif "Python" in query:
        sense = "Programming Language"
    
    print("Query:", query)
    print("Clicked Result:", result)
    print("Correct Sense:", sense)
    print()
