# example 1
age=int(input("Enter Age"))
if age >= 18:
  print("Eligible to Vote")
else:
  print("Not Eligibile to vote")

#example 2
m=int(input("Enter maths marks"))
c=int(input("Enter marks in chemistry"))
if(m>=50 and c>=50):
     print("pass")
else:
     print("Fail")

#example 3
m=int(input("Enter m values"))
i=1
while i<3:
    print(m)
    i+=1

#Example 4
n=int(input('Enter n value'))
i=1
while i<=10:
    print(n,"*",i,"=",(n*i))
    i+=1

#Example 5
pi=3.14
r=float(input("Enter Radius")) 
while r>0:
 print("Area is",(pi*r*r))
 r=float(input("Enter Radius"))
