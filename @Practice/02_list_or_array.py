countries = ["Pakistan", "India", "China", "United States", "United Kingdom"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Accessing elements of India
print(f"Country at index 1: {countries[1]}")

# Slicing the list
start = 0
end = 3
print(f"Numbers from index {start} to {end}: {numbers[start:end]}")


# Reversing the list
print(f"Reversed list: {countries[::-1]}")
print(f"Reversed list: {numbers[::-1]}")

# Appending a new element to the list
countries.append("Germany")
print(f"List after appending: {countries}")

# Removing an element from the list
countries.remove("Germany")
print(f"List after removing: {countries}")

# Inserting a new element at a specific index
countries.insert(2, "Germany")
print(f"List after inserting: {countries}")

# Extending the list with another list
countries.extend(["Germany", "France", "Italy"])
print(f"List after extending: {countries}")

# remove duplicate elements from the list
countries = list(set[str](countries))
print(f"List after removing duplicates: {countries}")

# shuffle the list
print(f"Shuffled list: {countries}")

print(f"List after shifting: {countries[0:len(countries) - 2]}")

# sort the list
countries.sort()
print(f"Sorted list: {countries}")
