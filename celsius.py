
# f = celcius*1.8 + 32

# celsius = float(input("Enter the temperature in Celsius: "))
#
# f = (celsius * 1.8) + 32
#
# print(f)

num = 32
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))