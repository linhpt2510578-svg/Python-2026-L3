num = int(input("Enter a number: "))

if num > 0:
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is NOT a perfect number")
else:
    print(f"{num} is NOT a perfect number")
