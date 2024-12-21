# test_script.py

def greet(name):
    message = f"Hello, {name}!"
    print(message)  

def add(a, b):
    try:
        result = int(a) + int(b)  
        print(f"The result is {result}")
    except ValueError:
        print("Error: Both inputs must be numbers.")

def divide(a, b):
    try:
        result = a / b 
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    greet("fahmy")
    add(3, "5") 
    divide(10, 0)

    print("All operations completed.")
