#write a programme to input the electricity unit charges and calculate the total electricity biill 

bill_units=float(input("enter the number of unit charges : "))
bill=0.0
if(bill_units<=50):
 bill +=bill_units*0.50
elif(bill_units<=150):
 bill+=(50*0.50)+((bill_units-50)*0.75)
elif(bill_units<=250):
 bill+=(50*0.50)+(100*0.75)+((bill_units-150)*1.20)  
else:
 bill+=(50*0.50)+(100*0.75)+(100*1.20)+((bill_units-250)*1.50)

bill+=bill*0.2

print(bill)
 