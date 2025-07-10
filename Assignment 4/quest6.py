#write a programme to check if a given number is prime number or not 

num=int(input("enter a number"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if(count>2):
    print("the number is not a prime number ")
else:
    print("the number is a prime number ")      
   
        