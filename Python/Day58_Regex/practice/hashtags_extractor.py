import re

tweet = "Learning #Python is fun! #coding #developer #BackendDev"
pattern = r"#\w+"

hashtags = re.findall(pattern, tweet)
print(f"Found hashtags: {hashtags}")