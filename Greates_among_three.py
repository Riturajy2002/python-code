a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print("{} is greater than {},{}".format(a,b,c)) 
elif b>a and b>c:
    print("{} is greater than {},{}".format(b,a,c)) 
else:
    print("{} is greater than {},{}".format(c,b,a)) 
    
