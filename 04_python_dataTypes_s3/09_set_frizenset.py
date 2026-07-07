odd_number = {1,3,5,7,9,11,13,15,17,19}
prime_number = {2,3,5,7,11,13,17,19}

# Union of two sets
union_numbers = odd_number | prime_number
print(f"Union of numbers: {union_numbers}")

# Intersection of two sets
intersection_numbers = odd_number & prime_number
print(f"Intersection of numbers: {intersection_numbers}")

# Difference of two sets
difference_numbers = odd_number - prime_number
print(f"Difference of numbers (odd - prime): {difference_numbers}")

# Symmetric difference of two sets
symmetric_difference_numbers = odd_number ^ prime_number
print(f"Symmetric difference of numbers: {symmetric_difference_numbers}")

