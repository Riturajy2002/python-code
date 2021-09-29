n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("The number {} is a perfect number".format(n))
else:
    print("The number {} is not a perfect number".format(n))
    