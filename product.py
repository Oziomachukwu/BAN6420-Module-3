# product.py
class Product:
    """
    Represents an insurance product with a unique ID, name, and price.
    """
    def __init__(self, product_id, name, price):
        if not isinstance(product_id, int) or not isinstance(name, str) or not isinstance(price, (int, float)):
            raise ValueError("Invalid product details")
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = True

    def update_price(self, new_price):
        """Updates the price of the product."""
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("Invalid price update")
        self.price = new_price
        print(f"Product {self.name} price updated to {self.price}.")

    def suspend(self):
        """Suspends the product, making it inactive."""
        self.active = False
        print(f"Product {self.name} has been suspended.")
    def reactivate(self):
        """Reactivates the product, making it active."""
        self.active = True
        print(f"Product {self.name} has been reactivated.")

