#Write a program to solve the following series :a. 1! + 2! + 3! + 4! + .....n!

num=int(input("enter the number till you want the addition"))

fact=1
sum_of_series=0
for i in range(1,num+1):
    fact=fact*i
    sum_of_series+=fact
print(f"factorial of number {num} is {fact} and sum of its series is {sum_of_series}")    
