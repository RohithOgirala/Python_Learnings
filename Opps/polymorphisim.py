# overiding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Demonstrating polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Output: Dog barks, Cat meows
