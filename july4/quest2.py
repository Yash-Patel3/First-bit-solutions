#programme for multiplication of rest to power number without using operator

a=int(input("enter a number = : "))
b=int(input("enter a number = : "))

ans=1

for i in range(1,b+1):
    ans=ans*a


print("ans is ",ans)