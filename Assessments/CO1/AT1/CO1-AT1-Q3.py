import re

reg_no = input("Enter Register Number: ")
email = input("Enter College Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

valid = True

# Register Number (Example: 22CS101)
if re.fullmatch(r"\d{2}[A-Z]{2}\d{3}", reg_no):
    print("Register Number : Valid")
else:
    print("Register Number : Invalid")
    valid = False

# Email
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@college\.edu", email):
    print("Email : Valid")
else:
    print("Email : Invalid")
    valid = False

# Course Code (Example: CS301)
if re.fullmatch(r"[A-Z]{2}\d{3}", course):
    print("Course Code : Valid")
else:
    print("Course Code : Invalid")
    valid = False

# Semester (1-8)
if re.fullmatch(r"[1-8]", semester):
    print("Semester : Valid")
else:
    print("Semester : Invalid")
    valid = False

# Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number : Valid")
else:
    print("Mobile Number : Invalid")
    valid = False

print("\n----- Registration Report -----")

if valid:
    print("Registration Successful")
else:
    print("Registration Failed")
