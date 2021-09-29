n=int(input("Enter the number:"))
orig=n
sum=0
for i in range(1,n+1):
    if(n%i==0):
        sum=sum+i
if(sum>orig):
    print("The {} is a Abundant number".format(orig))
else:
    print("The {} is not a Abundant number".format(orig))
