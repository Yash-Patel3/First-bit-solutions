#write a programme to input all the  angles of triangle and check whether triangle is valid or not 


angle1=int(input("enter the first angle of triangle: "))
angle2=int(input("enter the second  angle of triangle: "))
angle3=int(input("enter the third angle of triangle :" ))

allangles=angle1+angle2+angle3

if(allangles==180):
    print("the triangle is valid traingle")
else:
    print("triangle is invlaid traingle")    