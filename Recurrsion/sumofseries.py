
def SumOfSeries(n,sum):
    if n==0:
        return sum
    else:
        sum+=n
        return SumOfSeries(n-1,sum)



n=int(input("enter the range number"))
sum=0
result=SumOfSeries(n,sum)
print(result)