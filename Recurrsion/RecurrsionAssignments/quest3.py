#write a programme to reverse a number using the recurrsive fucntion

def reverseNumber(num,add=0):
    if num == 0:
        return add
    else:
        a=num%10
        add = add*10+a

        return reverseNumber(num//10,add)


num=int(input('enter a number : '))
result=reverseNumber(num)
print(result)