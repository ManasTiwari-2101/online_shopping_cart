class CartItem:
    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity

    def get_product(self):
        return self._product

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if quantity >= 0:
            self._quantity = quantity

    def get_subtotal(self):
        return self._product.get_price() * self._quantity

    def show(self):
        print(f"{self._product.get_name()} - Qty: {self._quantity}, Subtotal: ${self.get_subtotal():.2f}")
