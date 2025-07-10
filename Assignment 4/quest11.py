#check whether the given number is amstrong number or not

num=int(input("enter a number "))
temp=num
count=0

while(num!=0):
    number= num%10
    num=num//10
    count+=1

temp1=temp
sum=0

while(temp!=0):
    digit=temp%10

    power =1
    i=1
    while(i<=count):
        power*=digit
        i+=1
    temp=temp//10
    sum+=power

if sum==temp1:
    print("the given number is amstrong number")
else:
    print("the given number is not a mastrong number")         
