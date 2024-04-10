x = int(input("enter number for factorial:"))


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(x)
print("Factorial of ", x, " is ", result)
