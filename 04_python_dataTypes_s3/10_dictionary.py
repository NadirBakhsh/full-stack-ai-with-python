person = dict(type = "human", name = "John", age = 30) 
print(f"Person: {person}")

# initialize a dictionary
chai_recipe = {}

# set a value
chai_recipe['basae'] = 'black tea'
chai_recipe['liquid'] = 'milk'

#print the dictionary
print(f"Chai recipe: {chai_recipe}")

# remove a value
del chai_recipe['liquid']
print(f"Chai recipe after removing liquid: {chai_recipe}")

# is key exists
print(f"Is base key exists: {'base' in chai_recipe}")

# get keys
print(f"Keys: {chai_recipe.keys()}")

# get values
print(f"Values: {chai_recipe.values()}")

# get items
print(f"Items: {chai_recipe.items()}")

# get length
print(f"Length: {len(chai_recipe)}")

# get type
print(f"Type: {type(chai_recipe)}")

# pop a value
print(f"Popped value: {chai_recipe.popitem}")

# clear the dictionary
print(f"Cleared dictionary: {chai_recipe.clear()}")