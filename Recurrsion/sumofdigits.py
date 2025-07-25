def SumOfdigits(n,sum=0):
    if n==0:
     return sum
    else:
       a=n%10
       sum+=a
       n=n//10

       return SumOfdigits(n,sum) 



n=int(input("enter the digits : "))
result=SumOfdigits(n)
print(result)