# Simple demonstration of ambiguity handling

sentence = "She saw the man with a telescope"

print("Sentence:")
print(sentence)

print("\nCFG Possible Meanings:")
print("1. She used a telescope to see the man.")
print("2. The man has a telescope.")

# PCFG demonstration using probabilities
meaning1_probability = 0.7
meaning2_probability = 0.3

print("\nPCFG Probabilities:")
print("She used telescope:", meaning1_probability)
print("Man has telescope:", meaning2_probability)

if meaning1_probability > meaning2_probability:
    print("\nPCFG Selected Meaning:")
    print("She used a telescope to see the man.")
else:
    print("\nPCFG Selected Meaning:")
    print("The man has a telescope.")

# Simple neural parsing simulation
print("\nNeural Parsing:")
context = "She was looking through a telescope."

if "telescope" in context:
    print("Context suggests: She used a telescope to see the man.")
