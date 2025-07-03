#simple interest programme

principle=float(input("enter the principle amount : "))
rate=float(input("enter the rate : "))
time=float(input("enter the time required: "))

interest= (principle*rate*time)/100

print("interst calculated is : ",interest)