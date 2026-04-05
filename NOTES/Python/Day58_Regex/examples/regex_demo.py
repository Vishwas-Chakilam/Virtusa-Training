import re

text = "Contact me at alice@example.com or bob@test.org"
# Find all emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print("Found Emails:", emails)

# Mask emails
masked = re.sub(r'[\w\.-]+@[\w\.-]+', '[REDACTED]', text)
print("Masked text:", masked)