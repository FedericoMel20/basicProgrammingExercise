import operations as op

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {op.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {op.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {op.multiply(num1, num2)}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    print(f"{num1} / {num2} = {op.divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid choice! Please select a valid operation (1, 2, 3, or 4).")

if __name__ == "__main__":
    calculator()
