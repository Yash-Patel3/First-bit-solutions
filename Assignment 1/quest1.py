#write a programme to calculate the percentage of students based on marks of any 5 subjects

sub1=float(input("Enter the subject 1 marks:  "))
sub2=float(input("enter the subject 2 marks: "))
sub3=float(input("enter the subject 3 marks: "))
sub4=float(input("enter the subject 4 marks: "))
sub5=float(input("enter the subject 5 marks: "))

total_marks=sub1+sub2+sub3+sub4+sub5

percentage=(total_marks/500)*100

print("percaentage of student =  ",percentage)