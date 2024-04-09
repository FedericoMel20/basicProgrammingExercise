#Reverse a String by input your name
name = input("Enter your name: ")
reversed_name = ""

for char in name:
    reversed_name = char + reversed_name

print("Reversed name:", reversed_name)
