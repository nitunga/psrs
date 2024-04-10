x = int(input("Enter a number : "))

if x < 0:
    print("enter positive number")
else:
    sum_natural_number = 0
    while x > 0:
        sum_natural_number += x
        x -= 1
    print(sum_natural_number)
