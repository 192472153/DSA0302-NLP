import re

text = "My email is student@gmail.com"

match = re.search(r"[\w\.-]+@[\w\.-]+", text)

if match:
    print("Email Found:", match.group())
else:
    print("No Email Found")

Output:
Email Found: student@gmail.com
