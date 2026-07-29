import re

resume = """
Name: Rahul Sharma
Email: rahul@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

# Name
name = re.search(r"Name:\s*(.*)", resume)

# Email
email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)

# Mobile
mobile = re.search(r"\b[6-9]\d{9}\b", resume)

# Skills
skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
found_skills = []

for skill in skills:
    if re.search(skill, resume, re.IGNORECASE):
        found_skills.append(skill)

# Experience
experience = re.search(r"(\d+)\s+years", resume)

years = int(experience.group(1))

print("----- Candidate Summary -----")
print("Name :", name.group(1))
print("Email :", email.group())
print("Mobile :", mobile.group())
print("Skills :", ", ".join(found_skills))
print("Experience :", years, "Years")

# Eligibility
if years >= 2 and "Python" in found_skills:
    print("\nStatus : Eligible for Shortlisting")
else:
    print("\nStatus : Not Eligible")
