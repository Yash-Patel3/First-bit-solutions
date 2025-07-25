#write a rpogramme to print the fibonnachi series

def fibonachi(a,b,num):
    if num==0:
        return 
    c=a+b
    print(c)

    fibonachi(b,c,num-1)






num=int(input("enter a number range of series"))
if (num>1):
 a=0
 b=1
 print(a)
 print(b)
 fibonachi(a,b,num-2)

else:
   print(0)
    



