# multiple exceptions
name = 'rohit'
try:
    print(name + str(456))  # This will work
    print(10 / 0)  # This will cause a ZeroDivisionError
except NameError:
    print('Variable name is not defined')
except ZeroDivisionError:
    print('Division by zero error')


a=int(input('entr a number'))
b=int(input('enter another number'))
try:
    c=a/b
    print(c)
except ValueError:
    print('enter integer value')
except ZeroDivisionError:
    print('can not divisiable by zero')

