import re
text = "Alice: 400, Bob: 500, Charlie: 600."
# Using groups to extract numbers
amounts = re.findall(r"\d+", text)
print("Amounts:", amounts)