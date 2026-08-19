def greet_students(name, nChar):
    for i in range(nChar, 0, -1):
        print(name[0 : i])

name = input("Enter a Name: ")
greet_students(name, len(name))