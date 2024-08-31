import math

n = int(input())

is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{n} is prime')
else:
    print(f'{n} is not prime')



