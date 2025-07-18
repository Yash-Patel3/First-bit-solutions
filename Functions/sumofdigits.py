
def SumOfDigits(num):
    sum=0
    while(num!=0):
        a=num%10
        num=num//10
        sum+=a
    print(sum)    

num=629
SumOfDigits(num)
print(num)