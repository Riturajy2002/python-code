n=int(input("Enter the number:"))
orig=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r*r*r
    n=n//10
if(sum==orig):
    print("The number{} is armstrong ".format(orig))
else:
    print("The number{} is not armstrong ".format(orig))

