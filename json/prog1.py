# What is JSON?
#  JSON is just a way to store and send data in a simple text format. It 
#  sets are not used as  json

import json
x={ "name":"rohit","age":23,"city":"ongole"}
print(type(x))
y=json.dumps(x)
#What is json.dumps()?
#Purpose: Converts Python data into a JSON string.
#Why?: You need to change Python data (like dictionaries) into text (JSON) before you can send it over the internet or save it.
print(type(y))
z=json.loads(y)
print(type(z))
#What is json.loads()?
#Purpose: Converts JSON string back into Python data (like a dictionary).
#Why?: When you receive data in JSON format (from the internet or another app), you need to convert it back to Python to use it.

#Now, you can access values from the dictionary
print(z["name"])  # Output: rohit
print(z["age"])   # Output: 23
print(z["city"])  # Output: ongole

# you can  not access values y is in json  it is string format if u wnat to acessc convert to dictionary format
print(y["name"])  # Output: error
print(y["age"])   # Output:error
print(y["city"])  # Output: error