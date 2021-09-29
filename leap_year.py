year = int(input("Enter Year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes, {} is  Leap Year".format(year))
        else:
            print("No, {} is not a Leap Year".format(year))
    else:
        print("No, {} is not a Leap Year".format(year))
else:
    print("No, {} is not a Leap Year".format(year))
