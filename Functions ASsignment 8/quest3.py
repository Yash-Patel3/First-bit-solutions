def SumOfNumbers(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum    





num=int(input("enter a number "))
sum=SumOfNumbers(num)
print("sum of number is : ",sum)