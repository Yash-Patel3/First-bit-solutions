#write a programme to calculate days into years, weeks and days
total_days=int(input("enter the number of days: "))

total_years=total_days//365
reamining_days=total_days%365

weeks=reamining_days//7
days=reamining_days%7


print(f"{total_days} for approximately {total_years} years and {weeks} weeks and {days} no of days")