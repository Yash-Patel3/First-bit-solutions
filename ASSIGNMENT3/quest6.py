#write a programme to calculate the profit ort loss
sp =int (input("enter the selling price: "))
cp=int(input ("enter the cost price"))

if(sp>cp):
    print("its profit")
    profit=sp-cp
    print("profit is ", profit)

else:
    print("its loss") 
    loss=cp-sp
    print("loss is ",loss)   