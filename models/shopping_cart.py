from models.cart_item import CartItem
from models.product import Product, PhysicalProduct, DigitalProduct

class ShoppingCart:
    def __init__(self):
        self._items = {}
        self._catalog = {}

    def add_product_to_catalog(self, product):
        self._catalog[product.get_id()] = product

    def display_catalog(self):
        print("\nAvailable Products:")
        for product in self._catalog.values():
            product.display()

    def add_to_cart(self, product_id, quantity):
        if product_id in self._catalog:
            product = self._catalog[product_id]
            if product.get_quantity() >= quantity:
                product.update_quantity(-quantity)
                if product_id in self._items:
                    current = self._items[product_id].get_quantity()
                    self._items[product_id].set_quantity(current + quantity)
                else:
                    self._items[product_id] = CartItem(product, quantity)
                print("Added to cart.")
            else:
                print("Not enough stock.")
        else:
            print("Product not found.")

    def remove_from_cart(self, product_id):
        if product_id in self._items:
            item = self._items.pop(product_id)
            item.get_product().update_quantity(item.get_quantity())
            print("Item removed.")
        else:
            print("Item not in cart.")

    def update_cart_item(self, product_id, new_quantity):
        if product_id in self._items and new_quantity >= 0:
            item = self._items[product_id]
            difference = new_quantity - item.get_quantity()
            product = item.get_product()
            if product.get_quantity() >= difference:
                product.update_quantity(-difference)
                item.set_quantity(new_quantity)
                print("Quantity updated.")
            else:
                print("Not enough stock.")
        else:
            print("Invalid product or quantity.")

    def view_cart(self):
        print("\nCart Contents:")
        if not self._items:
            print("Cart is empty.")
            return
        total = 0
        for item in self._items.values():
            item.show()
            total += item.get_subtotal()
        print(f"Total: ${total:.2f}")
