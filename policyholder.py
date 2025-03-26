# policyholder.py
from product import Product
from datetime import datetime
class Policyholder:
    """
    Represents a policyholder who can register for products and manage their status.
    """
    def __init__(self, policyholder_id, name, status='Active'):
        if not isinstance(policyholder_id, int) or not isinstance(name, str):
            raise ValueError("Invalid policyholder details")
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.products = []
        self.payments = []
        self.amount_due = 0

    def register_product(self, product, due_date):
        """Registers a product for the policyholder if they are active."""
        self.due_date = due_date
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
        if not isinstance(product, Product):
            raise TypeError("Invalid product")
        if self.status == 'Active':
            self.products.append(product)
            self.amount_due += product.price
            print(f"{self.name} has been registered for {product.name}.")
        else:
            print(f"Cannot register product. {self.name} is {self.status}.")

    def suspend(self):
        """Suspends the policyholder."""
        if self.status == 'Suspended':
            raise RuntimeError(f"Policyholder {self.name} is already suspended.")
        else:
            self.status = 'Suspended'
            print(f"Policyholder {self.name} has been suspended.")
        

    def reactivate(self):
        """Reactivates the policyholder."""
        if self.status == 'Active':
            raise RuntimeError(f"Policyholder {self.name} is already active.")
        else:
            self.status = 'Active'
            print(f"Policyholder {self.name} has been reactivated.")

    def display_details(self):
        """Displays policyholder details."""
        print(f"ID: {self.policyholder_id}, Name: {self.name}, Status: {self.status}")
        print("Products:", ', '.join([product.name for product in self.products]) or "None")

