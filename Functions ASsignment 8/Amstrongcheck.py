#write a programme to check whether the given number is amstrong number or not

def CountOfNum(num):
    count=0
    while(num!=0):
        a=num%10
        count+=1
        num=num//10
    return count   
def AmstrongCheck(num,power):
    sum=0
    while num!=0:
        a=num%10
        sum+= (a**power)
        num=num//10
    return sum    


num=int(input("enter a number "))


count=CountOfNum(num)

result=AmstrongCheck(num,count)

if result==num:
    print("the given number is amstrong number ")
else:
    print("the gievn number is not amstrong number ")