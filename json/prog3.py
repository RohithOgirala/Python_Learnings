import json
x={
    "name":"Rohit",
    "age": 23,
    "marriage":True,
    "divorse":False,
    "Childern":("anny","billy"),
    "pets": None,
    "cars":[
        {"model":"Audi","colour":"red"} ,{"model":"tata","colour":"green"}
    ]
}
print(json.dumps(x))
print(json.dumps(x,indent=3,separators=(',', ':')))#If you add separators=(',', ':'), it removes the spaces around the commas (,) and colons (:), making the JSON more compact:


