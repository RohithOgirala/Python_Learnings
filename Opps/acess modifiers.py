# public
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public member
        self.model = model  # public member

    def display(self):  # public method
        print(f"Car brand: {self.brand}, Model: {self.model}")

# Creating an object of the class
car = Car("Toyota", "Corolla")

# Accessing public members
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Corolla
car.display()  # Output: Car brand: Toyota, Model: Corolla

# private
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand  # public member
        self.model = model  # public member
        self.__price = price  # private member with name mangling

    def display(self):
        print(f"Car brand: {self.brand}, Model: {self.model}, Price: {self.__price}")

    def get_price(self):  # public method to access private member
        return self.__price

# Creating an object of the class
car = Car("Toyota", "Corolla", 20000)

# Accessing public members
print(car.brand)  # Output: Toyota
print(car.model)  # Output: Corolla
car.display()  # Output: Car brand: Toyota, Model: Corolla, Price: 20000

# Accessing private member directly (this will cause an error)
# print(car.__price)  # AttributeError: 'Car' object has no attribute '__price'

# Correct way to access private member
print(car.get_price())  # Output: 20000


#protexted
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public member
        self._model = model  # protected member (by convention)

    def display(self):
        print(f"Car brand: {self.brand}, Model: {self._model}")

car = Car("Toyota", "Corolla")
print(car._model)  # Output: Corolla (accessible but should be avoided)
