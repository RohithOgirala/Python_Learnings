def function1(number):
    i=2
    count=0
    while (i>=1 and i<number):
        if number%i==0:
            count=count+1
        i=i+1
    if count==0:
     print("Prime")   
    else:
       print("Not Prime")

function1(5)      

# program to print reverse oreder

def reverseorder(arg):
   for x  in range(len(arg)-1,-1,-1):
     print(arg[x])
week=["sunday","monday","Tuesady"]
print(reverseorder(week))
 
    
 