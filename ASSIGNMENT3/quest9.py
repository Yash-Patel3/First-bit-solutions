#input five subjects marks from student and display it into grades

sub1=float(input("enter marks :"))
sub2=float(input("enter marks :"))
sub3=float(input("enter marks :"))
sub4=float(input("enter marks :"))
sub5=float(input("enter marks :"))

percentage=(sub1+sub2+sub3+sub4+sub5/500)*100

if percentage>=60:
    print("first class")
elif percentage>=50 and percentage<=59:
    print("second class")
else:
    print("fail")        