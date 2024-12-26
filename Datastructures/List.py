
a=['Rohit','Ram','Raju', 'Ravi']
print(type(a))# list

a.append('Rajesh') #inserted at the last 
print(a)#['Rohit', 'Ram', 'Raju', 'Ravi', 'Rajesh']


a.pop()#deletes the last element
print(a)#['Rohit', 'Ram', 'Raju', 'Ravi']

a.pop(2)
print(a)#['Rohit', 'Ram', 'Ravi']


b=['Apple','mango','Grapes','guva','orange']
print(b[0:4])#[Apple,mango,Grapes,guva]
print(b[0])#['guva]
print(b[1:2])#['mango']
print(b[2:4])#['Grapes', 'guva']
print(b[0:])#['Apple', 'mango', 'Grapes', 'guva', 'orange']
print(b)#['Apple', 'mango', 'Grapes', 'guva', 'orange']


