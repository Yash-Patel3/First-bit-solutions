
def CountNumber(num,count=0):
    if num==0:
        return count
    else:
        num=num//10
        count+=1

        return CountNumber(num,count)


def amstrong(num,power):
    if num==0:
        return 0
    else:
        a=num%10
       

        return a**power +amstrong(num//10,power)







num=int(input("enter a number : "))
count=CountNumber(num)
result=amstrong(num,count)

if result==num:
    print("the given number is amstrong number ")
else:
    print("the given number is not a amstrong number ")    