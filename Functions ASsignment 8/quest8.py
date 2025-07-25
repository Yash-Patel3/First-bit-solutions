#$write a programme to print the fibonnachi series 


def FibonnachiSeries(n):
    a=0
    b=1
    print(b)
    for i in range(2,num+1):
        c=a+b
        a=b
        b=c
        print(c)




num=int(input("enter the last number of the range : "))
FibonnachiSeries(num)