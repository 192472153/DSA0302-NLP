from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "Python is a programming language.",
    "Python is widely used for programming.",
    "Programming with Python is easy."
]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(text)

similarities = []

for i in range(len(text) - 1):
    score = cosine_similarity(vectors[i], vectors[i + 1])[0][0]
    similarities.append(score)

average_score = sum(similarities) / len(similarities)

print("Coherence Score:", round(average_score, 2))

if average_score > 0.3:
    print("The text is coherent.")
else:
    print("The text is less coherent.")
