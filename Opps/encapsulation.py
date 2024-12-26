class Car:
    def __init__(self, brand, model, price):
        self.brand = brand       # public attribute
        self.model = model       # public attribute
        self.__price = price     # private attribute (by convention)

    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Price: {self.__price}")

    def get_price(self):
        return self.__price  # Access private attribute using getter method

    def set_price(self, price):
        if price > 0:
            self.__price = price  # Set private attribute using setter method

car = Car("Toyota", "Corolla", 20000)
print(car.get_price())  # Output: 20000
car.set_price(25000)
print(car.get_price())  # Output: 25000
