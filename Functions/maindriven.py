#1 draw a pattern of pyrammid 5*5
# #check whether given number is perfect nmber 

# print table of given no
# print whtether the no is +ve or -ve or neutral
def pattern():
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ",end=" ")
        for j in range(1,i+1):
            print(" * ",end=" ")
        print()
def perfect(num):
    sum=0
    for i in range(1,num):
       if num%i==0:
         sum+=i
    if sum==num:
            return "the number is a perfect no"
    else:
            return "the number is not a perrfect no"    
def printTable(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i} ")

def checkNum():
    num=int(input("enter number : "))
    if(num>0):
        return "Number is positive"
    elif(num<0):
        return " Number is negative "
    else:
        return "Number is neutral"
    

    #main part
ch=0
while(ch!=5):
     ch=int(input("enter a number choice"))

     if ch==1:
        pattern()
     elif ch==2:
        num=int(input("entr a number"))
        ans=perfect(num)
        print(ans)
     elif ch==3:
        printTable(5)
     elif ch==4:
        ans=checkNum()
        print(ans)
     elif ch==5:
         print("No such item function in menu")  
         break 
     else:
         print("enter a valid number")    
    
                
