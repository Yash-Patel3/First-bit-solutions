
start=int(input("enter a number"))
stop=int(input("enter a number"))

for i in range(start,stop):
    if i%8==0:
        break
    else:
        print(i)