n = int(input())

for i in range(n + 1):
    spaces = (n - i) * ' '
    stars = i * '*'
    print(spaces, end='')
    print(stars, end='')
    print(' | ', end='')
    print(stars, end='')
    print()

# print((n + 1) * ' ', end='')
# print('|')
# for i in range(1, n + 1):
#     print((n - i) * ' ', end='')
#
#     for j in range(i):
#         print('*', end='')
#
#     print(' | ', end='')
#
#     for k in range(i):
#         print('*', end='')
#     print()
