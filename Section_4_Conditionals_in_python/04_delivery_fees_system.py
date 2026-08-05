order_amount = int(input("What is the order amount? "))

delivery_fee = 0 if order_amount > 300 else 10

print(f"Delivery fee: ${delivery_fee}")
