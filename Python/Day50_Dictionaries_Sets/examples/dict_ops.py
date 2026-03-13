student = {
    "name": "Jane",
    "id": 401,
    "courses": ["Math", "CS"]
}

print(student.get("name"))
# Add new key
student["grade"] = "A"

for k, v in student.items():
    print(f"{k} -> {v}")