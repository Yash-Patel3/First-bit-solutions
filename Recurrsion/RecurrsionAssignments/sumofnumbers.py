#write a programme to find the sum of n numbers using recurrsion

def SumOfNumbers(num):
    
    if num==0:
        return 0
    else:
        return num + SumOfNumbers(num-1)



num=int(input("'enter a number range"))

result=SumOfNumbers(num)
print(result)