def greet(person, message="Hello"):
    print(f"{message} {person}")

def add_numbers(x,y):
    return x+y

def print_args(*args):
    for arg in args:
        print(arg,end=" ")
    print()

def calculate_average(*args):
    avr=sum(args)/len(args)
    return avr

add=lambda x,y:x+y
square=lambda x: x**2
checker=lambda x: x%2==0

#trying all the functions
greet("mer")
xy=add_numbers(5,4)
print(xy)
print_args("Mer","yumi","mistre")
avr=calculate_average(5,4,3,4,3)
print(avr)
print(add(5,4))
print(square(6))
print(checker(9))


