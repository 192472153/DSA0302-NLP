import spacy

nlp = spacy.load("en_core_web_sm")

text = "Elon Musk is the CEO of Tesla and lives in the United States."

doc = nlp(text)

print("Named Entities:")

for entity in doc.ents:
    print(entity.text, ":", entity.label_)
