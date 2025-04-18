# This is a simple Python demo script for learning purposes.

# Function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python learning.")

# Function to demonstrate basic arithmetic operations
def arithmetic_demo(a, b):
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b if b != 0 else 'undefined (division by zero)'}")

# Function to demonstrate list operations
def list_demo():
    fruits = ["apple", "banana", "cherry"]
    print("Original list:", fruits)
    fruits.append("orange")
    print("After appending:", fruits)
    fruits.remove("banana")
    print("After removing 'banana':", fruits)

# Main function
def main():
    # Greeting
    greet_user("Student")

    # Arithmetic operations
    print("\nArithmetic Operations:")
    arithmetic_demo(10, 5)

    # List operations
    print("\nList Operations:")
    list_demo()

# Entry point of the script
if __name__ == "__main__":
    main()