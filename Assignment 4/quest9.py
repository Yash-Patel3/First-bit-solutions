start=int(input("enter a number : "))
stop=int(input("enter a number : "))

num=int(input("enter a number"))

for i in range(start,stop+1):
    if(i%num==0):
        print(i)