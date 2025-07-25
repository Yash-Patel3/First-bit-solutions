#write a programme to print the sum of digits using re3dcurrsion


def SumOfDigits(num):
    if num==0:
        return 0
    else:
        
        return num+ SumOfDigits(num-1)


num=int(input("enter the digits : "))

result=SumOfDigits(num)
print(result)