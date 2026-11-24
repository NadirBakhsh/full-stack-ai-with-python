# for loops
    for i in range(1,11):
        print(i)

# while loops
    while i < 11:
        print(i)
        i += 1

# nested loops
    for i in range(1,11):
        for j in range(1,11):
            print(i,j)
# break and continue
    for i in range(1,11):
        if i == 5:
            break
        print(i)
# pass
    for i in range(1,11):
        if i == 5:
            pass
        print(i)

# range
    for i in range(1,11):
        print(i)

# enumerate
    for i,j in enumerate(range(1,11)):
        print(i,j)

# zip
    for i,j in zip(range(1,11),range(11,21)):
        print(i,j)

# list comprehension
    [i for i in range(1,11)]
    [i for i in range(1,11) if i % 2 == 0]
    [i for i in range(1,11) if i % 2 != 0]
    [i for i in range(1,11) if i % 2 == 0]