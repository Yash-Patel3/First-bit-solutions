#write a programme to calculate m to the power n
def exponentOperation(m,n):
    if n==0:
        return 1
    else:
        return m * exponentOperation(m,n-1)
        




m=int(input("enter the base number : "))
n=int(input("enter the exponent number : "))


result=exponentOperation(m,n)
print(result)