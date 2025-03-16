from art import logo
def add(n1, n2):
    """Returns addition of two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Returns subtraction of first number with second number"""
    return n1 - n2

def multiply(n1, n2):
    """Returns multiplication of two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Returns division of first number with second number"""
    return n1 / n2

operations = \
    {"+":add,
     "-":subtract,
     "*":multiply,
     "/":divide}

def calculator(f_number, s_number, op):
    """Operations for users to pick and function
    will execute it to the 2 numbers included"""
    return operations[op](f_number, s_number)

print(logo)
def calculator_start():
    first_number = input("What's the first number: ")
    calculations = True
    while calculations == True:
        op = input("}\n-\n*\n/\nPick an operation: ")
        second_number = input("What's the next number: ")
        final_result = calculator(float(first_number), float(second_number), op)
        print(f"{first_number} {op} {second_number} '=' {final_result}")
        continue_calculations = input(f"Type 'y' to continue calculating with {final_result}, or type 'n' to start a new calculation: ")
        if continue_calculations == "y":
            first_number = final_result
        elif continue_calculations == "n":
            calculations = False
            calculator_start()

calculator_start()