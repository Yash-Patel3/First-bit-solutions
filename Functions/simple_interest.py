
def interest_amount(P,R,T):
    interest=(P*R*T)/100
    print(f"simple interst for given values is {interest}")



principle=float(input("Enter the principle amount"))
rate=float(input("enter the rate percent"))
time=float(input("enter the time"))

interest_amount(principle,rate,time)