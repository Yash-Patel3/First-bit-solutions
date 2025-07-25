#factorial sum
def FactorialSum(num):
    fact=1
    sum=0
    for i in range(1,num+1):
        fact*=i
        sum+=fact
    return sum    


num=int(input("Enter a number : "))
factorial=FactorialSum(num)
print("factorial of number is : ",factorial)