#write a programme to find the reverse of the number 


def reverseNumber(num):

    reverse=0
    while(num!=0):
     a=num%10
     reverse=reverse*10+a
     num=num//10

    return reverse 




num=int(input("enter a number "))

result=reverseNumber(num)

print(result)