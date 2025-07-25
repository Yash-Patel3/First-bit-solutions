#write a programme to check whether the number is prime or not using recurrsion

def primeNumCheck(num,i=2):
    if num==2:
        return True
    
    if  num==i:
         return True
    
    
    if num%i==0:

            return False
    return primeNumCheck(num,i+1)


num=int(input("enter a number :"))
if num==1:
    print("One is not a  prime")

result=primeNumCheck(num)

if result==True:
    print("the given number is prime number ")
else:
    print("the number is not a prime number")    

