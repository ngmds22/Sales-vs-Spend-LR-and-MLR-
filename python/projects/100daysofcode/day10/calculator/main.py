# Calculator
from art import logo

# Define operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return 'Error: Divide by zero'
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    
    should_continue = True

    while should_continue:
        operation_symbol = input("Enter operation symbol form the line above: ")

        while operation_symbol not in operations:
            print("Invalid operation symbol")
            operation_symbol = input("Enter operation symbol form the line above: ")

        num2 = float(input("Enter next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        user_choice = input("Would you like to continue(c), restart(r), or exit(e)?: ").lower()

        if user_choice == "c":
            num1 = answer
        elif user_choice == "r":
            should_continue = False
            print("Restarting...")
            calculator()
            break
        elif user_choice == "e":
            should_continue = False
            print("Exiting...")
        else:
            print("Invalid input")
        
calculator()