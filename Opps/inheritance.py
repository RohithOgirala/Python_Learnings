# init it is used to assign values sdirectly to the class members   with out defining in the class

class Student:
    def __init__(self,code,name):
        self.code=code
        self.name=name
    def show_data(self):
     print(self.code)
     print(self.name)
p=Student("rohit","python")
p.show_data()

p.code=input("enter code")
p.name=input("enter name")
p.show_data()

x=input("enter code")
y=input("enter name")
q=Student(x,y)
q.show_data()

