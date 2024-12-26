class Number:
    def __iter__(self):
        self.a = 1  # Start from 1 or any initial value
        self.c = int(input("Enter an increment value: "))  # Take increment input
        return self

    def __next__(self):
        if self.a <= 100:  # Stop iteration condition (e.g., up to 100)
            x = self.a
            self.a += self.c  # Increment by the value entered
            return x
        else:
            raise StopIteration

# Create an instance of the Number class
myclass = Number()
myiter = iter(myclass)

# Iterate using next()
for i in range(5):  # Display first 5 iterations
    print(next(myiter))

      