def CalTicket(no,src,dest,ticket):
   print(no)
   print(src)
   print(dest)
   print(ticket)



n=5
amt=100
src="Pune"
d="delhi"

#CalTicket(ticket=amt,dest=d,src=src,no=n)  #running
#CalTicket(src,ticket=amt,dest=d,no=n)  #not running
CalTicket(n,ticket=amt,dest=d,src=src)  # running
