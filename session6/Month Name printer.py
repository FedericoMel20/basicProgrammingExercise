def print_month_name(month_num):
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    if month_num >= 1 and month_num <= 12:
        print("Month:", month_names[month_num - 1])
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
print("Welcome! Here, you can check which age group you belong to")
while True:     
    print("1. Continue")
    print("2. Stop the program")
    choice = int(input("Please select 1 or 2: "))
    if choice == 1:
        month_num = int((input("Enter a number to see what month it corresponds to: ")))
        print_month_name(month_num)
    elif choice == 2:
        print("Thank you for using this program. I hope it was helpful. You can come back anytime.")
        break
    else:
         ("This input is invalid. Please choose option 1 or 2")
