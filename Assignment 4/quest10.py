#write a programme to check a given number is perfect number or not
num=int(input("enter a  number"))
sum=0
for i in range (1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print(f"the given number {num} is a perfect number ")   
else:
    print("the given number is not a perfect number ")     