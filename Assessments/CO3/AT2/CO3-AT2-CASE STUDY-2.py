print("CASE STUDY 2: AI-POWERED CUSTOMER SUPPORT CHATBOT")

# 1. POS Tagging
print("\n1. POS Tagging")

sentence1_words = ["Book", "a", "flight", "ticket", "now"]
sentence1_tags = ["VB", "DT", "NN", "NN", "RB"]

sentence2_words = ["This", "book", "is", "interesting"]
sentence2_tags = ["DT", "NN", "VBZ", "JJ"]

print("\nSentence 1:")
for word, tag in zip(sentence1_words, sentence1_tags):
    print(word, "/", tag)

print("\nSentence 2:")
for word, tag in zip(sentence2_words, sentence2_tags):
    print(word, "/", tag)


# 2. HMM Probability
print("\n2. HMM Probability")

p_book_vb = 0.6
p_book_nn = 0.4

p_start_vb = 0.5
p_start_nn = 0.5

verb_probability = p_start_vb * p_book_vb
noun_probability = p_start_nn * p_book_nn

print("Probability of Book as VB =", verb_probability)
print("Probability of Book as NN =", noun_probability)

if verb_probability > noun_probability:
    print("Final Tag: Book/VB")
else:
    print("Final Tag: Book/NN")


# 3. Rule-Based vs HMM Tagging
print("\n3. Rule-Based vs HMM Tagging")

word = "Book"

if word.lower() == "book":
    rule_tag = "VB"

print("Rule-Based Tag =", rule_tag)

if verb_probability > noun_probability:
    hmm_tag = "VB"
else:
    hmm_tag = "NN"

print("HMM Tag =", hmm_tag)


# 4. Intent Detection
print("\n4. Intent Detection")

sentence = "Book a flight ticket now"

if "Book" in sentence and "flight" in sentence:
    intent = "Flight Booking"
else:
    intent = "Unknown"

print("Sentence =", sentence)
print("Detected Intent =", intent)
