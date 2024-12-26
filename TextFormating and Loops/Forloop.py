# program 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#program 2
for l in range(5):  # Loops from 0 to 4
    print(l)

# program 3
for letter in "Python":
    print(letter)

# program 4
for s in range(1, 4):
    for k in range(1, 4):
        print(f"i={s}, j={k}")


# program 5
for i in range(1,20):
    code="RA23110030104"+str(i)
    print("Dear {},today we have a class on {}".format(code,"2.30") )

# program 6

students = [
    "Arjun", "Priya", "Rohan", "Anjali", "Sneha", 
    "Rahul", "Kavya", "Nikhil", "Meera", "Siddharth", 
    "Aditi", "Varun", "Pooja", "Akash", "Divya", 
    "Manish", "Shreya", "Vivek", "Neha", "Karan"
]
k=400
for j in range(len(students)):
  number="RA2311003010"+str(k+j)
  name=students[j]
  print("Dear {},Your Regno is {}".format(name,number))