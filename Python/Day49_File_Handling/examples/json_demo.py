import json

data = {
    "name": "Bruce",
    "role": "Batman",
    "skills": ["Martial Arts", "Detective"]
}

# Dump to JSON string
json_str = json.dumps(data, indent=4)
print(json_str)