sentence = ["Students", "study", "NLP"]

print("Sentence:", " ".join(sentence))


# Transition-Based Parsing
print("\nTransition-Based Parsing:")

stack = []
buffer = sentence.copy()

while buffer:
    word = buffer.pop(0)
    stack.append(word)
    print("SHIFT:", word)

print("\nDependency Relations:")
print("study --> Students (Subject)")
print("study --> NLP (Object)")


# Graph-Based Parsing
print("\nGraph-Based Parsing:")

words = ["Students", "study", "NLP"]

scores = {
    ("study", "Students"): 0.9,
    ("study", "NLP"): 0.95
}

print("Possible Dependency Scores:")

for relation, score in scores.items():
    print(relation, "Score:", score)

print("\nBest Dependency Tree:")
print("study --> Students (Subject)")
print("study --> NLP (Object)")
