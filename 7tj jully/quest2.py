num = int(input("Enter how many Fibonacci numbers to print: "))

a = 0
b = 1

print("Fibonacci series:")
for i in range(num):
    print(a)
    c = a + b
    a = b
    b = c
