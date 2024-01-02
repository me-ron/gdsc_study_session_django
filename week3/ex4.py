sum=count=0
for i in range(2,51,2):
    if i%3==0:
        count+=1
        print("three",end=" ")
    elif i%5==0:
        count+=1
        print("five",end=" ")
    else:
        print(i,end=" ")
    sum+=i
print()
print(f"sum={sum}")
print(f"count={count}")
    
    