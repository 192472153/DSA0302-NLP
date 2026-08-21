from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Natural language processing is interesting",
    "Python is useful for data science"
]

# User query
query = "Python programming"

# Create TF-IDF vectors
vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

# Calculate similarity
similarity_scores = cosine_similarity(
    query_vector,
    tfidf_matrix
).flatten()

# Sort documents based on score
ranked_documents = sorted(
    enumerate(similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

print("Document Ranking:")

for index, score in ranked_documents:
    print("Document:", documents[index])
    print("Score:", round(score, 2))
