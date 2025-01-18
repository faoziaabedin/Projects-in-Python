"""
CS1026a 2023
Assignment 04 Project - Shopping Cart
Faozia Abedin
251358351
fabedin4
December 8th, 2023
"""


# Class representing individual products in a store
class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Compare products based on name, price, and category
    def __eq__(self, other):
        if isinstance(other, Product):
            if ((self._name == other._name and self._price == other._price) and (self._category == other._category)):
                return True
            else:
                return False
        else:
            return False

    # Getter methods for product attributes
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # String representation of the Product
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep


# Class for inventory management
class Inventory:
    def __init__(self):
        self.inventory = {}  # Stores product details

    # Add a new product to the inventory
    def add_to_productInventory(self, productName, productPrice, productQuantity):
        product_info = self.inventory.get(productName, {})
        product_info['price'] = productPrice
        product_info['quantity'] = product_info.get('quantity', 0) + productQuantity
        self.inventory[productName] = product_info

    # Increment the quantity of a product
    def add_productQuantity(self, nameProduct, addQuantity):
        if nameProduct in self.inventory:
            self.inventory[nameProduct]['quantity'] += addQuantity

    # Decrement the quantity of a product
    def remove_productQuantity(self, nameProduct, removeQuantity):
        if nameProduct in self.inventory and self.inventory[nameProduct]['quantity'] >= removeQuantity:
            self.inventory[nameProduct]['quantity'] -= removeQuantity

    # Retrieve the price of a product
    def get_productPrice(self, nameProduct):
        return self.inventory.get(nameProduct, {}).get('price')

    # Retrieve the quantity of a product
    def get_productQuantity(self, nameProduct):
        return self.inventory.get(nameProduct, {}).get('quantity', 0)

    # Display the current state of the inventory
    def display_Inventory(self):
        for product, info in self.inventory.items():
            print(f"{product}, {int(info['price'])}, {info['quantity']}")


# Class for managing a shopping cart
class ShoppingCart:
    def __init__(self, buyerName, inventory):
        self.cart = {}
        self.buyerName = buyerName
        self.inventory = inventory

    # Add a product to the cart
    def add_to_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self.inventory.inventory:
            return "Product not in inventory"
        if self.inventory.inventory[nameProduct]['quantity'] < requestedQuantity:
            return "Can not fill the order"
        self.inventory.remove_productQuantity(nameProduct, requestedQuantity)
        if nameProduct in self.cart:
            self.cart[nameProduct] += requestedQuantity
        else:
            self.cart[nameProduct] = requestedQuantity
        return "Filled the order"

    # Remove a product from the cart
    def remove_from_cart(self, nameProduct, requestedQuantity):
        if nameProduct not in self.cart:
            return "Product not in the cart"
        if requestedQuantity > self.cart[nameProduct]:
            return "The requested quantity to be removed from cart exceeds what is in the cart"
        self.cart[nameProduct] -= requestedQuantity
        if self.cart[nameProduct] == 0:
            del self.cart[nameProduct]
        self.inventory.add_productQuantity(nameProduct, requestedQuantity)
        return "Successful"

    # Display the contents of the cart
    def view_cart(self):
        total_cost = 0
        for product, quantity in self.cart.items():
            price = self.inventory.get_productPrice(product)
            print(f"{product} {quantity}")
            total_cost += price * quantity
        print(f"Total: {int(total_cost)}")
        print(f"Buyer Name: {self.buyerName}")


# Class for managing a product catalog
class ProductCatalog:
    def __init__(self):
        self.catalog = []
        self.low_prices = set()
        self.medium_prices = set()
        self.high_prices = set()

    # Add a product to the catalog and categorize based on price
    def addProduct(self, product):
        for product in product:
            self.catalog.append(product)
            price = product['price']
            if 0 <= price <= 99:
                self.low_prices.add(product['name'])
            elif 100 <= price <= 499:
                self.medium_prices.add(product['name'])
            elif price >= 500:
                self.high_prices.add(product['name'])

    # Display the number of products in each price category
    def price_category(self):
        print(f"Number of low price items: {len(self.low_prices)}")
        print(f"Number of medium price items: {len(self.medium_prices)}")
        print(f"Number of high price items: {len(self.high_prices)}")

    # Display the complete catalog with detailed information
    def display_catalog(self):
        for product in self.catalog:
            print(f"Product: {product['name']} Price: {int(product['price'])} "
                  f"Category: {product['category']}")


# reads the files and populates the inventory
def populate_inventory(filename):
    inventory = Inventory()
    with open(filename, 'r') as file:
        for line in file:
            product_name, price, quantity, _ = line.strip().split(',')
            inventory.add_to_productInventory(product_name, float(price), int(quantity))
    return inventory


# reads the files and populates the catalog
def populate_catalog(fileName):
    catalog = ProductCatalog()
    products = []

    with open(fileName, 'r') as file:
        for line in file:
            name, price, _, category = line.strip().split(',')
            product = {'name': name, 'price': int(price), 'category': category}
            products.append(product)

    catalog.addProduct(products)
    return catalog
