#Implement a program that checks if a user's age is not less than 21
def federico(n):
    if n < 21:
        print("The number you", n, "inserted is less than 21")
    else:
        print("The number you inserted is not less than 21")
print("Hello, Welcome!\n")
a = int(input("Write the number you wish to compare with 21: "))
melchiorri = federico(a)
print(melchiorri)