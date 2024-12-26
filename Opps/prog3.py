class  student(object):
    def __init__(self,name):
        self.name=name
    def get_data(self):
        return self.name
class child(student):
    def __init__(self,name,age,city):
     super(). __init__(name)# super().__init__ 
     self.age=age
     self.city=city
    def insert(self,name,age,city):
       def __init__(self,name,age,city):
        super(). __init__(name)# super().__init__ 
        self.age=age
        self.city=city
    def display(self):
       return "my name is {},my age is {} ,my city is{}".format(self.name,self.age,self.city)
p=child("rohit",45,"ongole")
print(p.display())
          
    
          


 