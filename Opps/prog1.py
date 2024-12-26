class student:
     name="rohit"
     age=30
     city="ongole"
    

     def showdata(self):
        print("name is",self.name)
        print("age is",self.age)
        print("city is",self.city)

     def insert(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
p=student() 
p.showdata() 
p.insert("Rahul",25,"nellore") 
p.showdata() 

