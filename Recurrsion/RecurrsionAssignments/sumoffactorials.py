
def fact(num):
    if num==0 or num==1:
        return 1
    
    return num *fact(num-1)


def sumOfFactorials(num):
    if num==1:
        return fact(1)
    
    else:
        return fact(num) + sumOfFactorials(num-1)








num=int(input("enter a number range for factorial sum "))
result=sumOfFactorials(num)
print(result)