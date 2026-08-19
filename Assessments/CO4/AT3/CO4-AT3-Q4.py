# Feature Structure for Subject-Verb Agreement

subject = {
    "word": "She",
    "person": 3,
    "number": "singular"
}

verb = {
    "word": "writes",
    "person": 3,
    "number": "singular"
}

print("Feature Structure Checking:")

if subject["person"] == verb["person"] and subject["number"] == verb["number"]:
    print("Subject-Verb Agreement: Correct")
else:
    print("Subject-Verb Agreement: Incorrect")


# Subcategorization Frames

verb_frames = {
    "sleep": ["Subject"],
    "write": ["Subject", "Object"],
    "give": ["Subject", "Indirect Object", "Direct Object"]
}

print("\nSubcategorization Frames:")

for verb_name, arguments in verb_frames.items():
    print(verb_name, "requires:", ", ".join(arguments))
