class CosmeticItem:
    def __init__(self, name, cost_price, stock):
        self.name = name
        self.cost_price = cost_price
        self.stock = stock

class CosmeticShop:
    def __init__(self):
        self.items = {}
        self.transactions = []
        self.profits = 0

    def add_item(self, item):
        self.items[item.name] = item

    def display_items(self):
        print("Available Items:")
        for item_name, item in self.items.items():
            print(f"Name: {item.name}, Price: ${item.cost_price:.2f}, Stock: {item.stock}")

    def make_transaction(self, item_name, quantity):
        if item_name in self.items:
            item = self.items[item_name]
            if item.stock >= quantity:
                total_cost = item.cost_price * quantity
                item.stock -= quantity
                self.profits += total_cost
                self.transactions.append((item_name, quantity, total_cost))
                print(f"Transaction successful. You purchased {quantity} {item_name}(s) for ${total_cost:.2f}.")
            else:
                print("Insufficient stock.")
        else:
            print("Item not found.")

    def display_transactions(self):
        print("\nTransaction History:")
        for idx, (item_name, quantity, total_cost) in enumerate(self.transactions, start=1):
            print(f"{idx}. Purchased {quantity} {item_name}(s) for ${total_cost:.2f}")

    def display_profits(self):
        print(f"\nTotal Profits: ${self.profits:.2f}")

def main():
    shop = CosmeticShop()

    # Adding sample items
    shop.add_item(CosmeticItem("Lipstick", 10, 20))
    shop.add_item(CosmeticItem("Mascara", 15, 15))
    shop.add_item(CosmeticItem("Foundation", 20, 10))

    while True:
        print("\nWelcome to Siti's Cosmetic Shop")
        print("1. Display available items")
        print("2. Make a purchase")
        print("3. View transaction history")
        print("4. View total profits")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            shop.display_items()
        elif choice == '2':
            item_name = input("Enter the name of the item you want to purchase: ")
            quantity = int(input("Enter the quantity you want to purchase: "))
            shop.make_transaction(item_name, quantity)
        elif choice == '3':
            shop.display_transactions()
        elif choice == '4':
            shop.display_profits()
        elif choice == '5':
            print("Thank you for visiting Siti's Cosmetic Shop!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
