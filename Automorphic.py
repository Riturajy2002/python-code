n=int(input("Enter the number:"))
orig=n
sq=0
sq=n*n
r=orig%10
s=sq%10
if(r==s):
    print("The number {} is a automorphic number".format(n))
else:
    print("The number {} is not a automorphic number".format(n))
