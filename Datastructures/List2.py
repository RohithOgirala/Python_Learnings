# program to take input from user and display it

items=[]
n=int(input("Enter n value"))
for X in range(0,n+1):
    element=int(input("Enter elements"))
    items.append(element)
print(items)
#Enter n value 5    
#Enter elements11
##Enter elements34
#Enter elements2
#Enter elements45
#Enter elements67
#Enter elements90
#[11, 34, 2, 45, 67, 90]


#Program to take input from the user and print in reversr order
numbers=[]
m=int(input("Enter number of elemnts"))
for Y in range(0,m+1):
    values=int(input("Enter numbers"))
    numbers.append(values)
    numbers.sort()
print(numbers)
#output
#
"""
Enter number of elemnts 3
Enter numbers2
Enter numbers3
Enter numbers3
Enter numbers5
[2, 3, 3, 5]
"""
#prints in reverse order
numbers.reverse()
print(numbers)