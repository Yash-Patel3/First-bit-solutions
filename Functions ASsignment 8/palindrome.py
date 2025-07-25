
def PalindromeCheck(num):
    reversenum=0
    while(num!=0):
        a=num%10
        reversenum = reversenum*10+a
        num//=10

    return reversenum    




num=int(input("enter a number"))
result=PalindromeCheck(num)
if result==num:
    print("the gievn number is palindrome")
else:
    print("the gievn number is not a palindrome")    