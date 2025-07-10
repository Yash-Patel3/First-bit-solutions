#write a programm eto check whether the number is palindrome or not 

num_3_digit=int(input("enter three digit number : "))


hundreds=(num_3_digit%10)*100
tens=((num_3_digit//10)%10)*10
units=num_3_digit//100

total=hundreds+tens+units
if total==num_3_digit:
    print("number is palindrome")
else:
    print("nnumber is not palindrome")    