# Code Tracing Exercise
## Requirements
a. Find the syntax error and modify it. Please identify the error and what did you do to fix it?
b. The code should be able to display a given name as an inverted triangle, please fix the code in order for it to do that. See sample output below if entered name is Joseph
(insert example output)
## Code
```python
def greet_students(name, nChar):
    for i in range(nChar, 0, -1):
        print(name[0 : i])

name = input("Enter a Name: ")
greet_students(name, len(name))
```
