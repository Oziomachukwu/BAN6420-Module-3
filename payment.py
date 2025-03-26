# payment.py
from policyholder import Policyholder
from product import Product
from datetime import datetime

class Payment:
    """
    Represents a payment transaction for a policyholder purchasing a product.
    """
    def __init__(self, payment_id, policyholder, product, amount, payment_date):
        if not isinstance(policyholder, Policyholder) or not isinstance(product, Product) or not isinstance(amount, (int, float)):
            raise ValueError("Invalid payment details") # Validate input parameters
        
        self.payment_id = payment_id
        self.policyholder = policyholder
        self.product = product
        self.amount = amount
        self.status = "Pending"
        self.due_date = self.policyholder.due_date
        self.due_date = datetime.strptime(self.due_date, "%Y-%m-%d")
        self.payment_date = payment_date

    def apply_penalty(self):
        """Applies a penalty to the pending payment."""
        if self.status == "Overdue":
            self.policyholder.amount_due += 10  # Adding a penalty amount
            print(f"\nPenalty applied! New amount due: {self.policyholder.amount_due}")

    def process_payment(self):
        """Processes the payment if the policyholder and product are active."""
        self.payment_date = datetime.strptime(self.payment_date, "%Y-%m-%d")
        if self.payment_id in self.policyholder.payments: # Check if payment has already been processed
            raise RuntimeError("Payment already processed.") # Raise an error if payment has already been processed to avoid duplicating payments
        elif self.policyholder.status == 'Active' and self.product.active and self.payment_date > self.due_date: # Check if payment is overdue
            self.status = "Overdue"
            print(f"Payment of {self.amount} for {self.policyholder.name} is overdue. A penalty fee will apply") # Notify user of overdue payment 
            self.apply_penalty() #apply penalty
            self.policyholder.amount_due -= self.amount
            self.policyholder.payments.append(self.payment_id)    
            self.status = "Paid"
            if self.policyholder.amount_due <= 0:
                print(f"Payment of {self.amount} for {self.policyholder.name} has been processed.\n No outstanding balance.")
            else:
                print(f"Payment of {self.amount} for {self.policyholder.name} has been processed.\n Payment of {self.policyholder.amount_due} is still pending.")
        
        

        if self.policyholder.status == 'Active' and self.product.active and self.payment_date <= self.due_date:
            self.policyholder.amount_due -= self.amount
            self.policyholder.payments.append(self.payment_id)          
            self.status = "Paid"
            if self.policyholder.amount_due <= 0:
                print(f"Payment of {self.amount} for {self.policyholder.name} has been processed.\n No outstanding balance.")
            else:
                print(f"Payment of {self.amount} for {self.policyholder.name} has been processed.\n Payment of {self.policyholder.amount_due} is still pending.")
        

    def send_reminder(self): 
        """Sends a reminder if balance is still pending."""
        if self.policyholder.amount_due > 0:
            print(f"Reminder: Payment of {self.policyholder.amount_due} is due for {self.policyholder.name}.")
        else:
            print(f"No outstanding balance for {self.policyholder.name}.Reminder not required.")

   

