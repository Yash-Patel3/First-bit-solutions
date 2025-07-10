#write a programme to print all even number till n

num=int(input("enter a number: "))
for i in range(2,num+1):
    if i%2==0:
        print(i)
        