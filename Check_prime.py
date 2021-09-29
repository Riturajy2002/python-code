num=int(input("Enter the number Which you want to check:"))
count=0
for i in range(2,num+1):
    if(num%2==0):
        count=count+1
        break
if(count>2):
    print("the number is not a prime number")
else:
    print(" The number is prime number")