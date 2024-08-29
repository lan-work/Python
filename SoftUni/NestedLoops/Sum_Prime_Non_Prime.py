primes_sum = 0
non_primes_sum = 0

while True:
    action = input()

    if action == 'stop':
        break
    else:
        num = int(action)

    if num < 0:
        print('Number is negative.')
        continue

    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes_sum += num
    else:
        non_primes_sum += num

print(f'Sum of all prime numbers is: {primes_sum}')
print(f'Sum of all non prime numbers is: {non_primes_sum}')
