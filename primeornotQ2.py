from bdb import Breakpoint


x=int(input("Enter a number for prime or not--"))
for i in range(2,x):
    if x%i==0:
       print("not prime ")
       break
    else:
        print("prime")
    