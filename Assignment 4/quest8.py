# write a programm eto print which numbers are diivisible kby 7 and multiples of 5 in given range
start=int(input("enter a number: "))
stop=int(input("enter a number: "))

for i in range(start,stop+1):
    if i%7==0 and i%5==0:
        print(i)
