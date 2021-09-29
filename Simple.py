p=int(input("Enter the principle amount: "))
t=int(input("Enter the time in years:"))
r=int(input("Enter the rate per year:"))
simple_interest=(p*r*t)/100
print("The simple interest of {} in {} years with {}% rate is ={}".format(p,t,r,simple_interest))
