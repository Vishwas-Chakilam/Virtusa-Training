import re

text = "My phone number is 123-456-7890."
match = re.search(r"\d{3}-\d{3}-\d{4}", text)
if match:
    print("Phone Number found:", match.group())