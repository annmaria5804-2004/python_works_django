# create a class cart
# method1 : display the cart items enter by the user (self,items)
# method2: add items
# method3 : remove item
# method4 : calculate the total
 
class Cart:

    # Method 1: Display cart items
    def display(self, items):
        self.items = items
        print("Cart items:", self.items)

    # Method 2: Add items
    def add_items(self):
        item = input("Enter item to add: ")
        self.items.append(item)
        print(item, "added successfully")

    # Method 3: Remove items
    def remove_item(self):
        item = input("Enter item to remove: ")

        if item in self.items:
            self.items.remove(item)
            print(item, "removed successfully")
        else:
            print("Item not found")

    # Method 4: Calculate total
    def calculate_total(self, prices):
        total = sum(prices)
        print("Total amount:", total)


# Creating an object
obj1 = Cart()

# Getting items from user
items = input("Enter cart items separated by comma: ").split(",")

# Calling methods
obj1.display(items)
obj1.add_items()
obj1.remove_item()

# Getting prices
prices = [100, 200, 300]
obj1.calculate_total(prices)


# or price other way------------------------------------------------------------------------------------------------
class Cart:

    # Method 1: Display cart items
    def display(self):
        print("Cart Items:")
        for item, price in self.items.items():
            print(item, ":", price)

    # Method 2: Add items
    def add_items(self):
        item = input("Enter product name: ")
        price = int(input("Enter product price: "))

        self.items[item] = price
        print(item, "added successfully")

    # Method 3: Remove item
    def remove_item(self):
        item = input("Enter product to remove: ")

        if item in self.items:
            del self.items[item]
            print(item, "removed successfully")
        else:
            print("Item not found")

    # Method 4: Calculate total
    def calculate_total(self):
        total = sum(self.items.values())
        print("Total amount:", total)


# Creating object
obj1 = Cart()
obj1.items = {}

# Adding products
obj1.add_items()
obj1.add_items()

# Display cart
obj1.display()

# Calculate total
obj1.calculate_total()

# Remove product
obj1.remove_item()

# Display updated cart
obj1.display()
obj1.calculate_total()




# more than 2 items in cart in obj calling area-----------------------------------------------------------------------
class Cart:

    # Method 1: Display cart items
    def display(self, items):
        self.items = items

        print("Cart Items:")
        for item, price in self.items.items():
            print(item, ":", price)

    # Method 2: Add items
    def add_items(self):
        item = input("Enter product name: ")
        price = int(input("Enter product price: "))
        self.items[item] = price

    # Method 3: Remove item
    def remove_item(self):
        item = input("Enter product to remove: ")

        if item in self.items:
            del self.items[item]
            print("Item removed")
        else:
            print("Item not found")

    # Method 4: Calculate total
    def calculate_total(self):
        print("Total:", sum(self.items.values()))


# Creating object
obj1 = Cart()

# Passing multiple products with individual prices
obj1.display({
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Monitor": 12000,
    "Headphone": 1500,
    "Mobile": 20000
})

obj1.calculate_total()