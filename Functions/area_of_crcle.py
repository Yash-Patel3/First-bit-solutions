# write a function to print area of circle 

def area_circle(r):
    area=3.14*(r**2)
    print(f"Area of circle for radius {r} is {area}")
radius=int(input("enter the ardius of circle"))
area_circle(radius)