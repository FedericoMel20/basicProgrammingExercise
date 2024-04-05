def age_classifier(age):
    if age >= 0 and age <= 12:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

print("Welcome! Here, you can check which age group you belong to")
while True:     
    print("1. Continue")
    print("2. Stop the program")
    choice = int(input("Please select 1 or 2: "))
    if choice == 1:
        age = int((input("Enter your age: ")))
        age_group = age_classifier(age)
        print("You belong to the age group:", age_group)
    elif choice == 2:
        print("Thank you for using this program. I hope it was helpful. You can come back anytime.")
        break
    else:
         ("This input is invalid. Please choose option 1 or 2")