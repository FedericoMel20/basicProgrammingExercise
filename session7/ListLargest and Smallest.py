#Find the Largest and Smallest Number in a List [10, 20, 5, 40, 30, 72, 34]
numbers = [10, 20, 5, 40, 30, 72, 34]

# Initialize variables to hold the largest and smallest numbers
largest = numbers[0]
smallest = numbers[0]

# Iterate through the list
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
