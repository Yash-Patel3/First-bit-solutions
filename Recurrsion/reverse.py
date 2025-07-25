
def reverse(num,rev):
    if (num!=0):
        a=num%10
        rev=rev*10+a

        #call reverse function
        return  reverse(num//10,rev)
    
    else:
        return rev

num=int(input("enter a number : "))
result=reverse(num,0)
print(result)