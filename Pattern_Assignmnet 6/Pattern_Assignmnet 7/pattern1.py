# Upper part of the hollow diamond
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="   ")
        else:
            print(" ", end="   ")
    print()

# Lower part of the hollow diamond
for i in range(4, 0, -1):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="   ")
        else:
            print(" ", end="   ")
    print()
