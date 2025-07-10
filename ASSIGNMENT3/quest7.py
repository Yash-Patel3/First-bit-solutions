#write a programme to check is user has ewntered correct userid and passwordcorrect 
correct_userid="admin"
correct_password="4567@gmail.com"

user_id=input("enter the useid ")
password=input("enter the password ")

if user_id==correct_userid and password==correct_password:
  print("login succesfull")
else:
  print("Invalid login details")