


def LeapCheck(num):
    if (num%4==0 and num%100!=0) or (num%400==0):
        return True
    
    else:
        return False   
   





num=int(input("enter a year"))
result=LeapCheck(num)

if result==True:
    print("its a Leap year ")
else:
    print("Its not a Leap Year")    