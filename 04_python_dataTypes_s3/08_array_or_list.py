ingredients = ["milk", "sugar", "tea", "water"]

print(ingredients)

# Accessing elements
print(ingredients[0])
print(ingredients[1])

# Modifying elements
ingredients[0] = "coffee"
print(ingredients)

# Adding elements
ingredients.append("coffee")
print(ingredients)

# Removing elements
ingredients.remove("water")
print(ingredients)

# Length of the list
print(len(ingredients))

# Slicing the list
print(ingredients[0:2])

# Extending the list
ingredients.extend(["coffee", "water"])
print(ingredients)

# Inserting elements at a specific index
ingredients.insert(0, "sugar")
print(ingredients)

# Removing elements at a specific index
ingredients.pop(0)
print(ingredients)

# Removing elements at a specific index
ingredients.pop(0)
print(ingredients)

# Removing elements at a specific index
ingredients.pop(0)
print(ingredients)

# Sorting the list
ingredients.sort()
print(ingredients)

# Reversing the list
ingredients.reverse()
print(ingredients)


# Clearing the list
ingredients.clear()
print(ingredients)

# Copying the list
ingredients_copy = ingredients.copy()
print(ingredients_copy)

# Counting the number of elements in the list
print(ingredients.count("milk"))

# Finding the index of an element in the list
print(ingredients.index("milk"))

# Checking if an element is in the list
print("milk" in ingredients)

# Checking if an element is not in the list
print("milk" not in ingredients)

# Finding the maximum value in the list
print(max(ingredients))

# Finding the minimum value in the list
print(min(ingredients))

# Finding the sum of the list
print(sum(ingredients))

# Finding the average of the list
print(sum(ingredients) / len(ingredients))

# Finding the length of the list
print(len(ingredients))
