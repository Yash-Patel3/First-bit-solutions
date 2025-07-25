#sum of all prime numbers betweeen 1 to n

def PrimeNumberSum(num):
    sum=0
    
    for i in range(2,num):
        count=0
        for j in range (2,i):
            if i%j==0:
                count+=1
                break

        if count==0:
            sum+=i   
    
    return sum







num=int(input("Enter the number range : "))
result=PrimeNumberSum(num)
print(result)