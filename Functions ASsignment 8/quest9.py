#write afunction to find the sum of diigts of number 

def SumOfDigits(num):
    sum=0

    while(num!=0):
        a=num%10
        num=num//10
        sum+=a
    return sum

num=int(input("enter a number : "))
result=SumOfDigits(num)
print(result)