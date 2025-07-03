#programm eto calculate the quadratic roots of equation

a=float(input("enter the first coefficient number: "))
b=float(input("enter the 2nd coefficient number: "))
c=float(input("enter the 3rd coefficient number : "))

d=0.5*(b**2-4*a*c)

root1= (-b + d)/2*a
root2=(-b - d)/2*a


print("root1 = ",root1)
print("root2 =",root2)