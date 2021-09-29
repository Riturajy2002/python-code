n= int(input("Enter the number:"))
orig=n
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
if(orig%sum==0):
    print("The  {}  is a Harshad number ".format(orig))
else:
    print("The  {}  is not a Harshad number ".format(orig))