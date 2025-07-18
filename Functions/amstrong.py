def AmstrongNumber(n):
    amstrong = n
    count = 0

    # Count number of digits
    temp = n
    while temp != 0:
        temp = temp // 10
        count += 1

    # Calculate Armstrong sum
    temp = n
    sum = 0
    while temp != 0:
        digit = temp % 10
        sum += digit ** count
        temp = temp // 10

    # Check and return result
    if sum == amstrong:
        return "The given number is an Armstrong number."
    else:
        return "It's not an Armstrong number."


# Input from user
num = int(input("Enter a number: "))
print(AmstrongNumber(num))
