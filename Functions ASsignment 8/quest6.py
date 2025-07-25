


def SumOfOddNumbers(n):
    sum=0
    for i in range(2,n):
        if i%2!=0:
         sum+=i
    return sum    


num=int(input("enter the last range number"))
result=SumOfOddNumbers(num)
print(result)