student = {}

print("Menu")
print("1. Add a student\n2. View a student\n3. List all students\n4. Delete a student\n5. Exit")

choice = int(input())

while choice != 5:
    if choice == 1:
        print("Enter the name of the student:")
        name = input()
        print("Enter their age:")
        age = int(input())
        print("Enter their grade:")
        grade = float(input())
        student[name] = [age, grade]
    elif choice == 2:
        print("Which student do you want to view?")
        name = input()
        if name in student:
            print(f"Name: {name}, Age: {student[name][0]}, Grade: {student[name][1]}")
        else:
            print("Student not found.")
    elif choice == 3:
        for name in student:
            print(f"Name: {name}, Age: {student[name][0]}, Grade: {student[name][1]}")
    elif choice == 4:
        print("Which student do you want to delete?")
        name = input()
        if name in student:
            del student[name]
            print("successfully deleted")
        else:
            print("Student not found.")
        
    print("Make another choice:")
    choice = int(input())
