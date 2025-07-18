for i in range (1,6):
    for j in range (1,6-i):
        print(" ",end=" ")
    for j in range (1,i+1):
        if j==i or j==5:
         print(i ,end=" ")
        else:
           print(" ",end=" ") 
    print( )        