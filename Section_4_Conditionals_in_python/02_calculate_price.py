cup_size = input("What size of coffee do you want? (small, medium, large) ").lower()

small_price = 10
medium_price = 15
large_price = 20

if cup_size == "small":
    print(f"The price of the coffee is {small_price}")
elif cup_size == "medium":
    print(f"The price of the coffee is {medium_price}")
elif cup_size == "large":
    print(f"The price of the coffee is {large_price}")
else:
    print("Invalid cup size")