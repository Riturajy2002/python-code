n=int(input("Enter the number:"))
orig=n
sum=0
while(n>0):
    r=n%10
    sum=sum+(r**3)
    n=n//10
if(sum==orig):
    print(f"The number {orig} is armstrong.")
else:
    print(f"The number {orig} is not armstrong.")

