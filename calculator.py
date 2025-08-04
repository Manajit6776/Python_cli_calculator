def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def convert_input_into_float(input_value):
    try: # try exceot
        return float(input_value)
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculator():
    while True:
        print("\nOptions:")
        print("1. Add(+) ")
        print("2. Subtract(-) ")
        print("3. Multiply(*) ")
        print("4. Divide(/) ")
        print("5. Exit")

        choice = input("Enter choice (+ or - or * or / or q(to exit)): ")

        if choice.lower() == 'q':
            print("Exiting....")
            break

        if choice in ('+', '-', '*', '/'):
            num1 = convert_input_into_float(input("Enter first number: "))
            num2 = convert_input_into_float(input("Enter second number: "))

            if num1 is None or num2 is None:
                continue

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '/':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Welcome to the calculator program!")
    calculator()
    print("Exit successfully.")
