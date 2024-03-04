def sum_of_digits(n):
    # Convert the integer to a string to iterate through its digits
    digits = str(n)
    # Initialize sum
    digit_sum = 0
    # Iterate through each digit and add it to the sum
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum

num = int(input("Enter an integer: "))
print("Sum of digits:", sum_of_digits(num))
