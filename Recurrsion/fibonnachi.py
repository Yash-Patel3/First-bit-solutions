
def fibonnachi(a,b,n):
    if n==0:
        return 
    c=a+b
    print(c)
    fibonnachi(b,c,n-1)



n=int(input("enter a number : "))
a=0
b=1
print(a)
print(b)
fibonnachi(a,b,n-2)