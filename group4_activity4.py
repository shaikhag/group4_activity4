# Correcting the syntax error and continuing with the Cart class and main function implementation

class Cart:
    def __init__(self):
        self.list_of_purchased = []

    def addProduct(self, article_name, quantity):
        # Check if the article is in the INVENTORY
        if article_name in INVENTORY:
            # Check if the article is already in the cart
            for item in self.list_of_purchased:
                if item.getName() == article_name:
                    # Update the quantity if the item is already in the cart
                    available_quantity = INVENTORY[article_name].getQuantity()
                    add_quantity = min(quantity, available_quantity)
                    item.setQuantity(item.getQuantity() + add_quantity)
                    INVENTORY[article_name].setQuantity(available_quantity - add_quantity)
                    return
            # If the item is not in the cart, add it
            available_quantity = INVENTORY[article_name].getQuantity()
            if available_quantity >= quantity:
                self.list_of_purchased.append(Article(article_name, INVENTORY[article_name].getPrice(), quantity))
                INVENTORY[article_name].setQuantity(available_quantity - quantity)
            else:
                print(f"Only {available_quantity} available in the inventory. Adding {available_quantity} to the cart.")
                self.list_of_purchased.append(Article(article_name, INVENTORY[article_name].getPrice(), available_quantity))
                INVENTORY[article_name].setQuantity(0)
        else:
            print(f"Article {article_name} not found in the inventory.")

    def removeProduct(self, article_name, quantity):
        # Check if the article is in the cart
        for item in self.list_of_purchased:
            if item.getName() == article_name:
                if item.getQuantity() > quantity:
                    # Update the quantity if more than the specified quantity is in the cart
                    item.setQuantity(item.getQuantity() - quantity)
                    INVENTORY[article_name].setQuantity(INVENTORY[article_name].getQuantity() + quantity)
                    return
                else:
                    # Remove the item from the cart if the quantity to remove is equal to or greater than what's in the cart
                    self.list_of_purchased.remove(item)
                    INVENTORY[article_name].setQuantity(INVENTORY[article_name].getQuantity() + item.getQuantity())
                    return
        print(f"Article {article_name} not found in the cart.")

    def displayCart(self):
        if not self.list_of_purchased:
            print("Sorry the shopping cart is empty")
        else:
            for idx, item in enumerate(self.list_of_purchased, 1):
                print(f"Article {idx}: {item}")

    def checkout(self):
        total = 0
        for item in self.list_of_purchased:
            price = item.getPrice()
            if item.getQuantity() >= 3:
                price *= 0.9  # Apply discount
            total += price * item.getQuantity()
        total *= 1.07  # Apply VAT
        print(f"Your bill is {total:.2f}$")

# The main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            for article in INVENTORY.values():
                print(article)
        elif choice == "2":
            # Assume 'cart' is an instance of Cart
            cart.displayCart()
        elif choice == "3":
            article_name = input("Add an item from our catalogue to the shopping cart: ")
            quantity = int(input(f"Add the quantity of {article_name}: "))
            # Assume 'cart' is an instance of Cart
            cart.addProduct(article_name, quantity)
        elif choice == "4":
            article_name = input("Remove an item from the shopping cart: ")
            quantity = int(input(f"remove the quantity of {article_name} from the shopping cart: "))
            # Assume 'cart' is an instance of Cart
            cart.removeProduct(article_name, quantity)
        elif choice == "5":
            # Assume 'cart' is an instance of Cart
            cart.checkout()
        elif choice == "6":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

        continue_prompt = input("Do you want to continue (y/n): ").lower()
        if continue_prompt != 'y':
            print("Exiting the program. Goodbye!")
            break

# Correcting the undefined objects and other issues mentioned

# Global variable for cart to be accessed inside main and other functions
cart = Cart()

# Since the PCI does not support file operations, the following is a placeholder for read_data call
# The actual implementation should use a valid file path
def read_data_placeholder():
    # Placeholder data simulating the content of catalogue.csv
    catalogue_data = [
        ("iphone 15", 2349.0, 12),
        ("galaxy", 2700.0, 9),
        ("ipad 9th", 379.0, 5)
    ]
    for name, price, quantity in catalogue_data:
        INVENTORY[name] = Article(name, price, quantity)

# Function to simulate user interaction in place of 'input' calls
def simulate_input(display_text, predefined_answer):
    print(display_text)
    return predefined_answer

# Adjusting the main function to use simulate_input for demonstration
def main_simulation():
    read_data_placeholder()  # Simulating file read
    while True:
        display_menu()
        choice = simulate_input("Enter your choice: ", "1")
        if choice == "1":
            for article in INVENTORY.values():
                print(article)
        elif choice == "2":
            cart.displayCart()
        elif choice == "3":
            article_name = simulate_input("Add an item from our catalogue to the shopping cart: ", "iphone 15")
            quantity = int(simulate_input(f"Add the quantity of {article_name}: ", "3"))
            cart.addProduct(article_name, quantity)
        elif choice == "4":
            article_name = simulate_input("Remove an item from the shopping cart: ", "iphone 15")
            quantity = int(simulate_input(f"remove the quantity of {article_name} from the shopping cart: ", "1"))
            cart.removeProduct(article_name, quantity)
        elif choice == "5":
            cart.checkout()
        elif choice == "6":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")

        continue_prompt = simulate_input("Do you want to continue (y/n): ", "n").lower()
        if continue_prompt != 'y':
            print("Exiting the program. Goodbye!")
            break

# Commenting out the simulation function call for now
# main_simulation()

# The above simulation function replaces the use of 'input' calls and simulates user choices for demonstration purposes.


# Commenting out the main function call for now
# Since the PCI does not support file operations or input, the file reading and main loop cannot be run here.
read_data("C:\\Users\\nhatt\\OneDrive\\Documents\\python\\.vscode\\arrays\\products.csv")
cart = Cart()
main()
