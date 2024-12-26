class person(object):
    def __init__(self,name):
        self.name=name
class male(person):
    def __init__(self,name,gender,salaray):
        super().__init__(name)
        self.gender=gender
        self.salaray=salaray
    def display(self):
        return f"My name is {self.name}, my gender is {self.gender}, my salary is {self.salaray}"
class female(person):
    def __init__(self,name,gender,age):
        super().__init__(name)
        self.gender=gender
        self.age=age
    def show(self):
        return f"My name is {self.name}, my gender is {self.gender}, my age is {self.age}"
p=male("rohit","male",2300)   
print(p.display())
q=female("vyshu","female",67)
print(q.show())
      