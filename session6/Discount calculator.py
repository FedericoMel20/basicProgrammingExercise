def calculate_discounted_price(amount):
    if amount > 100:
        discount = 0.10  # 10% discount
    elif amount > 50:
        discount = 0.05  # 5% discount
    else:
        discount = 0  # No discount
    
    discounted_amount = amount - (amount * discount)
    return discounted_amount

print("Welcome! Here, you can calculate the discount you are entitled to and also know the new product price")
while True:     
    print("1. Continue")
    print("2. Stop the program")
    choice = int(input("Please select 1 or 2: "))
    if choice == 1:
        amount = float(input("Enter the purchase amount: $"))
        discounted_price = calculate_discounted_price(amount)
        if amount > 100:
            print("You are eligible for a 10 percent discount")
        elif amount > 50:
            print("You are eligible for a 5 percent discount")
        else:
            print("Sorry, you are not eligible for a discount") 
        print("Discounted price: $", discounted_price)
    elif choice == 2:
        print("Thank you for using this program. I hope it was helpful. You can come back anytime.")
        break
    else:
         ("This input is invalid. Please choose option 1 or 2")   