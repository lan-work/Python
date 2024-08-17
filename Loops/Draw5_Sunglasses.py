n = int(input())

stars = 2 * n
space = n

print(stars * '*', end='')
print(space * ' ', end='')
print(stars * '*')

for i in range(n - 2):
    print('*', end='')
    for j in range(2 * n - 2):
        print('/', end='')
    print('*', end='')

    if i == (n - 1) // 2 - 1:
        print(n * '|', end='')
    else:
        print(n * ' ', end='')

    print('*', end='')
    for k in range(2 * n - 2):
        print('/', end='')
    print('*', end='')

    print()

print(stars * '*', end='')
print(space * ' ', end='')
print(stars * '*')
