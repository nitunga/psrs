lower = int(input("enter lower limit : "))
upper = int(input("enter upper limit : "))
# if given a list of array ...
# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if the in range ...
# for num in range(lower,upper+1):
# total_sum = 0
# largest_prime = 0
# smallest_prime = float('inf')
prime_numbers = []
sum = 0
# for num in number:
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # print("is not prime number", num)
                prime_numbers.append(num)
                sum += num
                break
        else:
            # print()
            pass
            # break
            # total_sum += num
            # if num > largest_prime:
            #     largest_prime = num
            # if num < smallest_prime:
            #     smallest_prime = num
            # prime_numbers.append(num)

print(prime_numbers)
print(sum)
# print(total_sum)
# print("Largest prime number:", largest_prime)
# print("Smallest prime number:", smallest_prime)
