#write a function to print the factorial of a given number 

def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    print(f"factorial of a given number is {fact} ")
num=int(input("enter a number to find the factorial of : "))
factorial(num)        
