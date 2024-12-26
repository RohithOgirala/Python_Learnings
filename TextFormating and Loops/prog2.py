#  print given number is prime or not using While loop
n=int(input("Enter input value"))
i=2
count=0
while (i>1 and i<n):
    if n%i==0:
        count=count+1
        i+=1
if count==0:
    print("prime")
else:
    print("Not prime")
# using for loo]
m = int(input("Enter the m value: "))
cnt = 0

if m < 2:
    print("Not prime")  # Numbers less than 2 are not prime
else:
    for i in range(2, m):
        if m % i == 0:
            cnt += 1
            break  # No need to check further if a divisor is found
    if cnt == 0:
        print("Prime")
    else:
        print("Not prime")

        
