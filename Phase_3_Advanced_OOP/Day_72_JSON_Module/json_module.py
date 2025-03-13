# ============================================================
# Day 72: Working with JSON — loads, dumps & File Storage
# ============================================================

import json

# --- PYTHON DICT ↔ JSON ---
person = {
    "name"   : "Alice",
    "age"    : 28,
    "skills" : ["Python", "Flask", "SQL"],
    "active" : True,
    "score"  : 9.5,
    "address": {"city": "Mumbai", "pin": "400001"}
}

# json.dumps() → Python dict → JSON string
json_str = json.dumps(person, indent=4)
print("--- json.dumps ---")
print(json_str)
print(type(json_str))   # str

# json.loads() → JSON string → Python dict
python_obj = json.loads(json_str)
print("\n--- json.loads ---")
print(python_obj)
print(type(python_obj))   # dict
print("Name:", python_obj["name"])

# --- FILE I/O ---
# json.dump() → write to file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)
print("\n✅ Saved to person.json")

# json.load() → read from file
with open("person.json", "r") as f:
    loaded = json.load(f)
print("✅ Loaded from file:", loaded["name"], loaded["age"])

# --- WORKING WITH LISTS OF DICTS (common pattern) ---
students = [
    {"id": 1, "name": "Alice", "grade": "A"},
    {"id": 2, "name": "Bob",   "grade": "B"},
    {"id": 3, "name": "Charlie", "grade": "A+"},
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

with open("students.json") as f:
    data = json.load(f)

print(f"\n--- Students ({len(data)} records) ---")
for s in data:
    print(f"  {s['id']}. {s['name']} — {s['grade']}")

# --- CUSTOM SERIALIZATION (for non-serializable objects) ---
import datetime

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return super().default(obj)

event = {"name": "PyCon", "date": datetime.date(2026, 6, 15)}
print("\nDate as JSON:", json.dumps(event, cls=DateEncoder))

# Cleanup
import os
os.remove("person.json")
os.remove("students.json")
