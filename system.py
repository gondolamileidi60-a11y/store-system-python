from user_manager import UserManager
from product import Product
from cart import Cart

class StoreSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.products = [
            Product(1, "Laptop", 850),
            Product(2, "Mouse", 20),
            Product(3, "Keyboard", 35),
            Product(4, "Headphones", 50)
        ]
        self.current_user = None
        self.cart = Cart()

    def show_products(self):
        for product in self.products:
            print(product)

    def store_menu(self):
        while True:
            print("\n--- STORE MENU ---")
            print("1. View product list")
            print("2. Add product to cart")
            print("3. View cart")
            print("4. Clear cart")
            print("5. Logout")

            option = input("Select option: ")

            if option == "1":
                self.show_products()

            elif option == "2":
                self.show_products()
                try:
                    product_id = int(input("Product ID: "))
                    quantity = int(input("Quantity: "))

                    for product in self.products:
                        if product.id == product_id:
                            self.cart.add_product(product, quantity)
                            print("Product added to cart.")
                            break
                    else:
                        print("Invalid product ID.")
                except:
                    print("Invalid input.")

            elif option == "3":
                self.cart.view_cart()

            elif option == "4":
                self.cart.clear_cart()

            elif option == "5":
                self.current_user = None
                self.cart = Cart()
                print("Logged out.")
                break

            else:
                print("Invalid option.")
