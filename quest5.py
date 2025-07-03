#compound interest programme
principle=float(input("enter the principle amount : "))
rate=float(input("enter the rate : "))
time=float(input("enter the time required: "))

compund_interest=principle *(1+rate/100)**time

print("compund interest amount is: ", compund_interest)