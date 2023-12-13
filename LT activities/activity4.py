print("enter a sentence:")
sentence=input().split()
print(*[len(i) for i in sentence])