#write a rogramme to reverse three digit number


num=int(input("enter three digit number = "))

hundreds=(num%10)*100
tens=((num//10)%10)*10
units=(num//100)

reversenumber=hundreds+tens+units

print(f"reverse of number {num} is {reversenumber}")