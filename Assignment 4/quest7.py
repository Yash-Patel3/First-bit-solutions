# write a programme to print all integers upto n that are not divisible by  2 and 3

num=int(input("enter a number :"))

for i in range(1,num+1):
    if i%2!=0 and i%3!=0:
        print(i)