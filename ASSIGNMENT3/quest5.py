#write a programme to check whether the traingle is issosceles ,scalene or euilateral

side1=int(input("enter the first side: "))
side2=int(input("enter the second side: "))
third=int(input("enter the third side: "))


if (side1==side2==third):
    print(" the given triagnle is equilateral traingle")
elif(side1==side2 != third or side2==third != side1 or third==side1!=side2):
    print("the triangle is isosceleous triangle ")
else:
    print("the triangle is scalene triangle ")     