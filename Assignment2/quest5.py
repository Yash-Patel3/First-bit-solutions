#calculate the selling price of book if its cost price and discount amount is given 

cost_price=float(input("enter the cost price of book : "))
discount_rate=float(input("enter the discount rate : "))


disscount_price=(discount_rate/100)*cost_price
selling_price=cost_price-disscount_price

print("the selling rpice of book is ",selling_price)