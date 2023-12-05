print("enter the word: ")
word=input()
if word==word[::-1]:
    print(f"The word {word} is palindrome.")
else:
    print(f"The word {word} is not palindrome.\nBecause {word[::-1]} is not equal to {word}.")
