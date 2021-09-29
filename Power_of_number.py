base=int(input("Enter the base number:"))
expo=int(input("Enter the exponent of the number:"))
temp=1
for i in range(0,expo):
    temp=temp*base
print("The power of {} is = {}".format(base,temp))
