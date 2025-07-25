
def ExponentialSums(n):
    exponent=0
    
    for i in range(1,n+1):
        exponent+=i**i
    return exponent    

num=int(input("enter the number : "))
result=ExponentialSums(num)
print("the sum of all numbers is : ",result)

