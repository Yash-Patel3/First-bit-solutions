#programme to find the sum of 3 digit number



num=int(input("enter the three digit number: "))

sum=0
while(num != 0):
    sum += num % 10
    num=num//10


print("sum of three digit number is: ",sum)    