#convert distance given in feet and inches into e metres and centimeter

feet=int(input("enter the number of feet = "))
inches=int(input("enter the number of inches = "))


feet_into_metres=feet*0.3048
inches_into_centimeter=inches*2.54


print(f"the number if meters is {feet_into_metres} and the number of insches is {inches_into_centimeter}")