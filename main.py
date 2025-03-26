# main.py
from policyholder import Policyholder
from product import Product
from payment import Payment
import datetime
try:
    # Create Products
    health_insurance = Product(101, "Health Insurance", 500)
    car_insurance = Product(102, "Car Insurance", 300)

    # Create Policyholders
    salim = Policyholder(1008, "Salim Adelarin")
    emeka = Policyholder(1009, "Emeka Jideofor")

    # Register Policyholders for Products
    salim.register_product(health_insurance, "2023-10-01")
    emeka.register_product(car_insurance, "2023-10-01")

    # Process Payments
    payment1 = Payment("P1012",salim, health_insurance, 500, "2023-09-20") #payment made before due date
    payment2 = Payment("P1013",emeka, car_insurance, 300, "2023-10-03") #payment made after due date
    
    payment1.process_payment() #process payment for salim
    payment2.process_payment() #process payment for emeka

    # Display Policyholder Details
    salim.display_details()
    emeka.display_details()

    # Generate a payment reminder for Salim if he hasn't paid
    payment1.send_reminder()

    # Suspend and Reactivate Policyholder
    emeka.suspend()
    emeka.display_details()
    emeka.reactivate()
    emeka.display_details()

except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
