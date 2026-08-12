from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
stemmer = PorterStemmer()
documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]
# Stem before vectorization
processed = []
for doc in documents:
    words = doc.lower().split()
    stems = [stemmer.stem(word) for word in words]
    processed.append(" ".join(stems))
print("Processed Documents:")
for doc in processed:
    print(doc)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(processed)
print("\nVocabulary:")
print(vectorizer.get_feature_names_out())

