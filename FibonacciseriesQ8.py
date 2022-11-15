x=int(input("Enter a number for fibonacci series--"))
a,b=0,1
while x:
    x=a,b
    x=a,a+b
    print(x,end=" ")
    
    