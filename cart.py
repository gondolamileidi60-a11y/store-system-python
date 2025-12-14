class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        total = 0
        for product, quantity in self.items:
            subtotal = product.price * quantity
            total += subtotal
            print(f"{product.name} x{quantity} = ${subtotal:.2f}")

        print(f"Total: ${total:.2f}")

    def clear_cart(self):
        self.items.clear()
        print("Cart cleared.")
