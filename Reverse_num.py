a=int(input("Enter the number:"))
reverse=0
while(a>0):
    r=a%10
    reverse=reverse*10+r   
    a=a//10
print("The reverse number is ={}".format(reverse))
