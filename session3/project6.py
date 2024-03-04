def check(n):
    if n % 2 == 0:
        print("The number you inserted is an even number")
    else:
        print("The number you inserted is an odd number")
    if n >= 10:
        print("The number is greater than 10 as well")
    else:
        print("This number is NOT more than 10")

print("Hello, Welcome!\n")
a = int(input("Write the number here: "))
result = check(a)
print(result)      