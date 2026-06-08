import sys
# floating and decimal number

milk_quantity = 1.5    # float (liters)
sugar_quantity = 0.75  # float (kg)

total_ingredients = milk_quantity + sugar_quantity

print(f"Total (milk + sugar): {total_ingredients}")

# Floating-point arithmetic
a = 0.1
b = 0.2
c = a + b
print(f"0.1 + 0.2 = {c}")  # May not exactly be 0.3 due to floating-point representation

# For more accurate decimal calculations, use the decimal module
from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.2')
z = x + y
print(f"Using Decimal: 0.1 + 0.2 = {z}")  # Precise decimal result

# More float arithmetic operations
float_division = 7 / 3
print(f"7 / 3 = {float_division}")  # Outputs: 2.333...

# Floor division with floats
float_floor_division = 7 // 3
print(f"7 // 3 = {float_floor_division}")  # Outputs: 2.0

# Type Checking
print(f"Type of milk_quantity: {type(milk_quantity)}")    # <class 'float'>
print(f"Type of x: {type(x)}")                            # <class 'decimal.Decimal'>


print(sys.float_info)  # print the floating-point precision and range