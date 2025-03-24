import json
data = '{"name": "Zarnigor", "age": 18}'
parsed_data = json.loads(data)  # Converts JSON string to Python dict
print(parsed_data["name"])  # Output: Zarnigor
