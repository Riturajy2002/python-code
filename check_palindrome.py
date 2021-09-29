a=int(input("Enter the number:"))
orig=a
reverse=0
while(a>0):
    r=a%10
    reverse=reverse*10+r
    a=a//10
if(reverse==orig):
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome number")