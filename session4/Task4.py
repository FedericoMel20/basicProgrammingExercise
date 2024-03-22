#Welcome Message
print("\nWelcome! Here, you can calculate the price of your product which will be determined by 10% what you bought it.")
#Loop to keep the program going for as long as the user wants
while True:
    print("\n1. Continue ")
    print("2. Stop the program")

    selected_option = int(input("\nSelect option 1 or 2: "))
    if selected_option == 1:
        cost = int(input("Input the cost of the product: "))
        price = round(0.1 * cost)

        print("The price you should sell this product is ", price)

    elif selected_option == 2:
        print("Thank you and Goodbye!")
        break
    
    else:
        print("choose the correct option")    

