# Parent class

# hierarchical inheritance is implemented by having multiple child classes inherit from a single parent class. 
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Child class 1
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__
        self.breed = breed

    def bark(self):
        print(f"{self.name}, the {self.breed}, barks: Woof Woof!")

# Child class 2
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the parent class's __init__
        self.color = color

    def meow(self):
        print(f"{self.name}, the {self.color} cat, meows: Meow Meow!")

# Creating objects for each class
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Kitty", "white")

# Accessing methods and attributes
dog.sound()  # Output: Buddy makes a sound.
dog.bark()   # Output: Buddy, the Golden Retriever, barks: Woof Woof!

cat.sound()  # Output: Kitty makes a sound.
cat.meow()   # Output: Kitty, the white cat, meows: Meow Meow!
