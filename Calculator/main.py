from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
input_one = float(input("What's the firse number? "))
continue_calculating = True

while continue_calculating == True:
    
    not_valid_operation = True
    while not_valid_operation:
        operation = input("+ \n- \n* \n/ \nPick an operation: ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            not_valid_operation = False
        else:
            print("Please give a valid operation!")
    input_two = float(input("What's the next number? "))
    output = operations[operation](input_one,input_two)
    print(f"{input_one} {operation} {input_two} = {output}")
    not_valid_response = True
    while not_valid_response:
        response = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation or type 's' to stop calculating.\n")
        if response == "y" or response == "n" or response == "s":
            not_valid_response = False
        else:
            print("Please give a valid response!")
    if response == "y":
        input_one = output
    elif response == "n":
        input_one = float(input("What's the firse number? "))
    else:
        continue_calculating = False