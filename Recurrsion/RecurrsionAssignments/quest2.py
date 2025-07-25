
def CountOfNumber(num,count=0):
    if num==0:
        return count
    else:
        a=num%10
        count+=1

        return CountOfNumber(num//10,count)

def amstrongNumberCheck(num,power):
    if num==0:
        return 0
    else:
        a=num%10
        
        return a**power + amstrongNumberCheck(num//10,power)


num=int(input("enter a number : "))
count=CountOfNumber(num)

result=amstrongNumberCheck(num,count)


if (result==num):
    print("the given number is amstrong number ")
else:
    print("The given Number is not a amstrong Number ")    