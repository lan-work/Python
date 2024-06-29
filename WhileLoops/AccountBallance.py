deposit = input()
deposit_total = 0

while deposit != 'NoMoreMoney':
    deposit_current = float(deposit)

    if deposit_current < 0:
        print(f'Invalid operation!')
        break

    print(f'Increase: {deposit_current:.2f}')
    deposit_total += deposit_current
    deposit = input()

print(f'Total: {deposit_total:.2f}')

