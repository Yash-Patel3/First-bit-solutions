#write a programme to input all sides triangle and chech whether a triangle is valid or not 

a=int(input("enter the side of triangle : "))
b=int(input("enter the side of triangle : "))
c=int(input("enter the side of triangle : "))


if (a+b>c and a+c>b and b+c>a):
    print("the triangle is valid ")
else:
    print("triangle is invalid")    
