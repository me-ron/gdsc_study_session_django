lst=[i for i in range(100)]

evens=list(filter(lambda x:x%2==0,lst))
print(evens)

doubles=list(map(lambda x:x*2,lst))
print(doubles)

def sum(x,y):
    try:
        int(x) + int(y)
    except ValueError:
        print("Invalid input value")
    else:
        print(x+y)
x=int(input())
y=int(input())
print(sum(x,y))

def divide(x,y):
    try:
        x/y
    except ZeroDivisionError:
        print("you are trying to divide by zero")
    else:
        print(x/y)
x=int(input())
y=int(input())
print(divide(x,y))
