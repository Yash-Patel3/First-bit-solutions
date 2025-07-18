
for i in range(1, 6):
    # Print spaces
    for j in range(1, 6-i):
        print(" ", end=" ")

    # Print increasing numbers
    num = i
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1

    # Print decreasing numbers
    num -= 2  # Adjust to start from one less than last printed
    for j in range(1, i):
        print(num, end=" ")
        num -= 1

    print()
