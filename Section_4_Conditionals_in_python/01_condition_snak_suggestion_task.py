snak_name = input("What is your snake's name? ").lower()

if snak_name == "cookie" or snak_name == "samosa":
    print(f"Great Choice! {snak_name} is a great snake!")
elif snak_name == "python":
    print(f"Python is a great snake!")
else:
    print(f"I don't know much about {snak_name}, but I'm sure it's a great snake!")
