def PrimeOrNot():
  num=int(input("enter a number"))
  if num%2!=0:
    return "its a prime "
  else:
    return "its not a prime number"


num=PrimeOrNot()
print(num)    