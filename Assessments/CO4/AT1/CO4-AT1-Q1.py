# Semantic Representation in Customer Support Chatbot

queries = [
    ("Activate international roaming", "ACTIVATE", "Roaming"),
    ("Deactivate caller tune service", "DEACTIVATE", "CallerTune"),
    ("Check my data balance", "QUERY", "DataBalance"),
    ("Enable 5G service", "ACTIVATE", "5GService")
]

print("Semantic Representations:\n")

for query, action, obj in queries:
    print(query)
    print(action + "(" + obj + ", Customer)")
    print()
