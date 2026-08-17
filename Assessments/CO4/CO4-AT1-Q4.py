# Syntax-Driven Semantic Analysis

sentences = [
    "Doctor prescribed medicine to patient",
    "Patient reported severe headache",
    "Nurse monitored patient continuously",
    "Medicine reduced blood pressure"
]

roles = {
    "Doctor": "Agent",
    "Medicine": "Instrument",
    "Patient": "Recipient",
    "Headache": "Symptom"
}

print("Parsed Sentences:\n")

for sentence in sentences:
    print(sentence)
    print("Parse Structure: Subject-Verb-Object")

print("\nSemantic Roles:\n")

for entity, role in roles.items():
    print(entity, "->", role)
