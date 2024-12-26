# no return type no argumnets
def display():#f unction deleration
    print("Hello World")

display()  #function call

#Function with arguments and  relturn type
#example 1
def show(name):
    name=input("Enter name")
    print("My Name is",name)

show("name")

# example 2
def function1(number):
   print(number)
function1("ram")   

# example 3
def function2(age=60):
    print(" I am ",age,"old")
function2(99)   # over rides the value and prints I am 99 old
function2()# I am 60 old(if you not pass any arguments it takes default arguments)

# example 4
def function3(args):
    for x in args:
     print(x)
list=["Apple","Mango","Orange","Grapes"]
function3(list)

# arguments pass and return values
def function5(a,b,c):
   return a+b+c
x=int(input("Enter X vlaue"))
y=int(input("Enter y value"))
z=int(input("Enter z value"))
print(function5(x,y,z))

def function6(city):
   strname=input("Enter city")
   print("I live in"+strname,end=" ")
function6("instant")




