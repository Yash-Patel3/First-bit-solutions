#write a programme to check userid and password is correct if correct generate a random captcha and give a prompt to user that login is successful  

import random
import string

correct_userid="admin"
correct_password="4567@gmail.com"

user_id=input("enter the useid ")
password=input("enter the password ")


if user_id==correct_userid and password==correct_password :
    captcha= "".join(random.choices(string.ascii_letters+string.digits,k=5))

    print(f"captcha: {captcha}")


    entered_captcha=input("enter the captch: ")

    if captcha==entered_captcha:
        print("login successfull")
    else:
        print("enter the valid captcha")
else:
    print("wrong userid or password")            