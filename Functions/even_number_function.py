#write a function to print even number in given range 
def even_number(l,h):
    for i in range(l,h):
        if i%2==0:
            print(i)


start=int(input("enter a starting number "))
end=int(input('enter a endfing number'))

even_number(start,end)
