print("enter the range:")
n=int(input())
for i in range(1,n+1):
    if i%15==0:
        print("FIZZBUZZ",end=" ")
    elif i%5==0:
        print("BUZZ",end=" ")
    elif i%3==0:
        print("FIZZ",end=" ")
    else:
        print(i,end=" ")
