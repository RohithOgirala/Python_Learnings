vehicle={
    "model":"hero",
    "price":4500,
    "color":"red"
}
print(vehicle)


x=vehicle['model']
print(x)

# gets the value  
y=vehicle.get("model")
print(y)

# update the value
vehicle['price']=5000
print(vehicle)

# add new key and value
vehicle['year']=2003
print(vehicle)

#prints value
for values in vehicle:
    print(vehicle[values])

# prints key 
for key in vehicle:
    print(key)

# prints the both
for key,values in vehicle.items():
    print(key,values)

# removes key and value
vehicle.pop('model')
print(vehicle)

# removes lat added item
vehicle.popitem()
for k,v in vehicle.items():
    print(k,v)