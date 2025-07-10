# Check Armstrong numbers in a given range

start = int(input("Enter a starting number: "))
stop = int(input("Enter a stopping number: "))

print(f"\nArmstrong numbers between {start} and {stop} are:")

for num in range(start, stop + 1):
    temp = num
    count = 0

    # Count digits
    while temp != 0:
        temp = temp // 10
        count += 1

    temp = num
    sum = 0

    # Sum of powers of digits
    while temp != 0:
        digit = temp % 10
        power = 1
        for i in range(count):
            power *= digit
        sum += power
        temp = temp // 10

    # Check Armstrong condition
    if sum == num:
        print(num)
