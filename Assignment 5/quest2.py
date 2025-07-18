#enter a number of students from user for those many students take marks of five subject calculate their percentage and calculate the avergae percentage
num=int(input("enter the number of students "))
sum_of_percenatge=0
for i in range (1,num+1):
    sub1=int(input("enter the marks of subject 1"))
    sub2=int(input("enter the marks of subject 1"))
    sub3=int(input("enter the marks of subject 1"))
    sub4=int(input("enter the marks of subject 1"))
    sub5=int(input("enter the marks of subject 1"))

    percentage=((sub1+sub2+sub3+sub4+sub5)/500)*100
    sum_of_percenatge+=percentage

print("avergae percentage of all students")
average=sum_of_percenatge/num

print(f"average percenatge of all students is {average}")