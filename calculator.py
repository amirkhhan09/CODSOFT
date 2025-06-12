# calculator.py

# 🔸 Author: Amir Khan
# 🔸 Internship: CodSoft (Python Programming)
# 🔸 Task 2: Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

def calculator():
    print("🧮 Welcome to the Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❗ Invalid input. Please enter numeric values.")
        return

    print("\nSelect an operation:")
    print("1 ➕ Addition")
    print("2 ➖ Subtraction")
    print("3 ✖️ Multiplication")
    print("4 ➗ Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'
    else:
        print("❌ Invalid choice.")
        return

    print(f"\n✅ Result: {num1} {op} {num2} = {result}")

calculator()
