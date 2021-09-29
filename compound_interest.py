import math
p=int(input("Enter the principle amount:"))
r=int(input("Enter rate  per year:"))
t=int(input("Ente the time in year:"))
A=p*(math.pow((1+r/100),t))
CI=A-p
print("The compound interest is= {}".format(CI))
