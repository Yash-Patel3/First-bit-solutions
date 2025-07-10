#write a programme to print fibonnachi series upto n 
num= int(input("entr a number : "))

a=0
b=1

for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
