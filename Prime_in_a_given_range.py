start=int(input("Enter starting range:"))
end=int(input("Enter ending range:"))
for i in range(start,end):
    for j in range(2,i+1):
        if i%2==0:
            break
    else:
        print("{} is a prime number ".format(i))
    

