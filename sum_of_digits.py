a=int(input("Enter the digits:"))
sum=0
while(a>0):
    sum=sum+a%10
    a=a//10
print("Sum of digits={}".format(sum))