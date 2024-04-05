a = 0
b = 0

def sum(a, b):
    return a + b
def difference(a, b):
    return a - b
def product(a, b):
    return a * b
def divide(a, b) :
    return a / b
print("Welcome! Here, you can calculate simple operations on any two numbers. ")
while True:
    print("1. Continue")
    print("2. Stop the calculator")
    choice = int(input("Please select 1 or 2: "))
    if choice == 1:
        num1 = float(input("Please insert the first number: "))
        operator = input("Please input the operator symbol (+, *, /, -): ")
        num2 = float(input("Please write the second number to see the result: "))
        if operator == '+':
            print("The result is: ", sum(num1, num2))
        elif operator == '-':
            print("The result is: ", difference(num1, num2))
        elif operator == '*':
            print("The result is: ", product(num1, num2))
        elif operator == '/':
            if num2 == 0:
                print("Error, division by zero")
            else:    
                print("The result is: ", divide(num1, num2))
        else:
            print("This operator is not recognized. Please insert a correct operator")
    elif choice == 2:
        print("Thank you for using this calculator.")
        break
    else:
        print("Please choose number 1 or 2. Your input is invalid")
