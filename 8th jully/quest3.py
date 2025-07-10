#print even number using the while loop
start=int(input("enter a number :"))
stop=int(input("enter a number :"))

while(start<stop):
    if start%2==0:
        print(start)
    start+=1    