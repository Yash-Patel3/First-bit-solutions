#convert the time entered in hr in minutes and seconds

total_seconds=int(input("enter the total seconds: "))

total_hours= total_seconds//3600
minutes= (total_seconds%3600)//60
seconds=total_seconds%60

print(f"for {total_seconds} total seconds there are {total_hours} total hours {minutes} and {seconds} seconds  ")
