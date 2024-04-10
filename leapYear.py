year = int(input("Enter year to check if it is leap or not: "))

if year % 400 == 0 and year % 100 == 0:
    print("{0} is a Leap year".format(year))
elif year % 4 == 0 and year % 100 != 0:
    print("{0} is a Leap year".format(year))
else:
    print("{0} is Not a leap".format(year))
