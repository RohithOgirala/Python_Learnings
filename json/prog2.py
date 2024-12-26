import json
print(json.dumps({"name":"jon","age":23}))
print(json.dumps(["apple","bananas"]))# Python list, which is an ordered collection, can be converted into a JSON array (an ordered list of values).
print(json.dumps(42))## Converts integer to JSON number
print(json.dumps(3.14)) # Converts float to JSON number
print(json.dumps(True))# Converts boolean True to JSON true
print(json.dumps(False)) # Converts boolean False to JSON fals
print(json.dumps(None)) # # Converts None to JSON null

a=json.loads('{"name":"rohit","city":"ongole"}')# Convert a JSON string back to a Python object (dictionary)
print(a)
print(type(a)) # This will print the type of 'a', which is a dictionary