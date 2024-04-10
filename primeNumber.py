x = int(input("Enter a prime number: "))

if x == 0:
    print("No prime")
elif x > 2:
    for i in range(2, x):
        if (x % i) == 0:
            print(x, "is Not a prime number")
            break
    else:
        print(x, "is Prime Number")
else:
    print(x, "is Not prime number")
