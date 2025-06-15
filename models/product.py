from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity

    def get_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def update_quantity(self, amount):
        if self._quantity + amount >= 0:
            self._quantity += amount

    @abstractmethod
    def display(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self._weight = weight

    def display(self):
        print(f"[Physical] ID: {self._product_id}, Name: {self._name}, "
              f"Price: ${self._price}, Qty: {self._quantity}, Weight: {self._weight}kg")


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, download_link):
        super().__init__(product_id, name, price, quantity)
        self._link = download_link

    def display(self):
        print(f"[Digital] ID: {self._product_id}, Name: {self._name}, "
              f"Price: ${self._price}, Qty: {self._quantity}, Link: {self._link}")
