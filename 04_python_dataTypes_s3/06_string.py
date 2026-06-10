user_name = "Nadir Bakhsh"

print(f"User name: {user_name}")

# Indexing
print(f"First character: {user_name[0]}") # N
print(f"Last character: {user_name[1]}") # a
print(f"Last character: {user_name[2]}") # d
print(f"Last character: {user_name[3]}") # i
print(f"Last character: {user_name[4]}") # r

#  Reverse Indexing
print(f"Reverse indexing: {user_name[-1]}") # h
print(f"Reverse indexing: {user_name[-2]}") # a
print(f"Reverse indexing: {user_name[-3]}") # d
print(f"Reverse indexing: {user_name[-4]}") # i
print(f"Reverse indexing: {user_name[-5]}") # r
print(f"Reverse indexing: {user_name[-6]}") # a
print(f"Reverse indexing: {user_name[-7]}") # d
print(f"Reverse indexing: {user_name[-8]}") # i
print(f"Reverse indexing: {user_name[-9]}") # r
print(f"Reverse indexing: {user_name[-10]}") # a
print(f"Reverse indexing: {user_name[-11]}") # N

# Skipping characters
print(f"Skipping characters: {user_name[::2]}") # Ndir Bakhsh
print(f"Skipping characters: {user_name[1::2]}") # dirBakhsh

#  Encoding and Decoding String

lable_text = "Hello, World!"
encoded_text = lable_text.encode('utf-8')
print(f"Encoded text: {encoded_text}")

decoded_text = encoded_text.decode('utf-8')
print(f"Decoded text: {decoded_text}")

# Slicing String

sliced_text = user_name[0:5]
print(f"Sliced text: {sliced_text}")    # Nadir

sliced_text = user_name[6:11]
print(f"Sliced text: {sliced_text}")    # Bakhsh

sliced_text = user_name[12:17]
print(f"Sliced text: {sliced_text}")    # Bakhsh


