from models.shopping_cart import ShoppingCart
from models.product import PhysicalProduct, DigitalProduct

def main():
    cart = ShoppingCart()

    # Adding sample products
    cart.add_product_to_catalog(PhysicalProduct("P101", "Headphones", 50.0, 10, 0.2))
    cart.add_product_to_catalog(DigitalProduct("D202", "Antivirus Software", 29.99, 50, "http://download.com/av"))

    while True:
        print("\n--- Menu ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart Item")
        print("5. Remove from Cart")
        print("6. Exit")

        choice = input("Choice: ")

        if choice == "1":
            cart.display_catalog()
        elif choice == "2":
            pid = input("Enter Product ID: ")
            qty = int(input("Enter Quantity: "))
            cart.add_to_cart(pid, qty)
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            pid = input("Product ID to update: ")
            qty = int(input("New Quantity: "))
            cart.update_cart_item(pid, qty)
        elif choice == "5":
            pid = input("Product ID to remove: ")
            cart.remove_from_cart(pid)
        elif choice == "6":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
