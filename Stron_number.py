n=int(input("Enter the  number:"))
orig=n
sum=0
while(n):
    r=n%10
    n=n//10
    fact=1
    for j in range(1,r+1):
        fact=fact*j
    sum=sum+fact
    
if(orig==sum):
    print("The number {} is strong number".format(orig))
else:
    print("The number {} is not strong number".format(orig))
