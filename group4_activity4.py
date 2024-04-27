# Importing the csv module to read the catalogue data
import csv

class Article:
    """
    Represents an article in the inventory or cart with a name, price, and quantity.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Article: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}"

# Placeholder for the global INVENTORY dictionary
INVENTORY = {}

def read_data(file_path):
    """
    Reads the data from a CSV file and stores it in the global INVENTORY dictionary.
    """
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Skip the headers
        for row in csvreader:
            name, price, quantity = row
            INVENTORY[name] = Article(name, float(price), int(quantity))

def display_menu():
    """
    Displays the main menu options to the user.
    """
    menu = """
    1. List all items, inventory and price
    2. List cart shopping items
    3. Add an item to the shopping cart
    4. Remove an item from the shopping cart
    5. Checkout
    6. Exit
    """
    print(menu.strip())

class Cart:
    """
    Represents a shopping cart, which is capable of adding and removing articles, 
    displaying its contents, and checking out.
    """
    def __init__(self):
        self.list_of_purchased = []

    def addProduct(self, article_name, quantity):
        if article_name in INVENTORY:
            article = INVENTORY[article_name]
            if quantity <= article.getQuantity():
                # Check if article is already in the cart
                for purchased in self.list_of_purchased:
                    if purchased.getName() == article_name:
                        purchased.setQuantity(purchased.getQuantity() + quantity)
                        article.setQuantity(article.getQuantity() - quantity)
                        return
                # If not in the cart, add new entry
                self.list_of_purchased.append(Article(article_name, article.getPrice(), quantity))
                article.setQuantity(article.getQuantity() - quantity)
            else:
                print(f"Not enough inventory for {article_name}.")
        else:
            print(f"Article {article_name} not found in inventory.")

    def removeProduct(self, article_name, quantity):
        for purchased in self.list_of_purchased:
            if purchased.getName() == article_name:
                if quantity < purchased.getQuantity():
                    purchased.setQuantity(purchased.getQuantity() - quantity)
                    INVENTORY[article_name].setQuantity(INVENTORY[article_name].getQuantity() + quantity)
                elif quantity >= purchased.getQuantity():
                    self.list_of_purchased.remove(purchased)
                    INVENTORY[article_name].setQuantity(INVENTORY[article_name].getQuantity() + purchased.getQuantity())
                return
        print(f"Article {article_name} not found in cart.")

    def displayCart(self):
        if not self.list_of_purchased:
            print("Sorry the shopping cart is empty")
        else:
            for article in self.list_of_purchased:
                print(article)

    def checkout(self):
        total = sum(item.getPrice() * item.getQuantity() * (0.9 if item.getQuantity() >= 3 else 1) for item in self.list_of_purchased)
        total *= 1.07  # Apply 7% VAT
        print(f"Your bill is {total:.2f}$")

def main():
    """
    The main function to run the shopping cart program.
    """
    read_data('catalogue.csv')  # Replace with the correct path to the CSV file
    cart = Cart()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            for article in INVENTORY.values():
                print(article)
        elif choice == "2":
            cart.displayCart()
        elif choice == "3":
            article_name = input("Add an item from our catalogue to the shopping cart: ")
            quantity = int(input(f"Add the quantity of {article_name}: "))
            cart.addProduct(article_name, quantity)
        elif choice == "4":
            article_name = input("Remove an item from the shopping cart: ")
            quantity = int(input(f"Remove the quantity of {article_name} from the shopping cart: "))
            cart.removeProduct(article_name
