#write a programme to input userid and password and check whether it is valid or not if not give a user chance to input user id and password for three times

""""
userid = "admin"
password = "admin@123"
count=1

while(count<=3):
 input_userid=str(input("enter your userid :  "))
 input_password=str(input("enter your passwrod : "))
 if userid==input_userid and password==input_password :
  print('login successfull')
  break
 else:
  print ("invalid userid or password please try again")
  count+=1


else:
 print("you have tried too many time login attempts")


"""
userid = "admin"
password = "admin@123"
count = 1

while count <= 3:
    input_userid = input("Enter your userid: ")
    input_password = input("Enter your password: ")

    if userid == input_userid and password == input_password:
        print("Login successful")
        break
    else:
        print("Invalid userid or password. Please try again.")
        count += 1
else:
    print("You have tried too many login attempts. Access denied.")
