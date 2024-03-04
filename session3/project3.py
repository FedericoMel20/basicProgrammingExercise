print("\nWelcome, find out if your age is eligible for voting")
age = int(input("Please write your age here: "))
if age >= 18 and age <= 65:
    print("Congratulations, your age is within the voting range and you are eligible to vote")
else:
    print("I'm sorry, your age is not eligible for voting")
    print("To be eligible, you have to be at least 18 and at most 65 years old")
