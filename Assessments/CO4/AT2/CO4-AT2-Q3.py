# Medical report input
text = """The doctor who reviewed the patient last week
recommends starting medication and scheduling a follow-up visit in Chennai."""

print("Medical Report:")
print(text)

# Convert text to lowercase
text = text.lower()

# Extract basic information
doctor = "Doctor"
patient = "Patient"

# Find actions
actions = []

if "starting medication" in text:
    actions.append("Start medication")

if "scheduling a follow-up visit" in text:
    actions.append("Schedule follow-up visit")

# Find time
if "last week" in text:
    time = "Last week"
else:
    time = "Not specified"

# Find location
if "chennai" in text:
    location = "Chennai"
else:
    location = "Not specified"

# Display result
print("\n--- Extracted Information ---")

print("Doctor:", doctor)
print("Patient:", patient)
print("Diagnosis: Not specified")
print("Time:", time)

print("\nActions:")
for action in actions:
    print("-", action)

print("\nLocation:", location)
