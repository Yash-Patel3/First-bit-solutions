num=int(input('enter a number to calculate the facctorial of'))
fact=1

for i in range (2,num+1):
    fact=fact*i
 
print(f"factorial of number {num} is  ",fact)