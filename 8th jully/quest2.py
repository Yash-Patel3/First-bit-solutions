#write a programme to print number that are not divisible by 8

start=int(input("enter a number starting"))
stop=int(input("enter a stopping number"))


for i in range(start,stop+1):
    if i%8==0:
     continue
    else:
       print(i)
