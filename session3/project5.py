def compare(a,b):
    if a == b:
        print("The two numbers you inserted are equal")
    elif a > b:
        print("The number ", a, "is bigger than the number ", b)
    else:
        print("The number ", b, "is bigger than the number ", a)
print("Hello, Welcome. We can help you compare two integers\n") 
a = int(input("insert the first number here: "))
b = int(input("insert the second number here: "))
result = compare(a,b)
print(result)