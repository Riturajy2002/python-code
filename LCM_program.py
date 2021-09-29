num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second Number:"))


def lcmFinder(num1, num2):
    if num1 > num2:
        larger = num1
    else:
        larger = num2
    while True:
        if (larger % num1 == 0) and (larger % num2 == 0):
            lcm = larger
            break
        larger = larger + 1
    print("LCM of two given number:{}".format(lcm))


lcmFinder(num1, num2)
