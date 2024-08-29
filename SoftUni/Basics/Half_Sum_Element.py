import sys

n = int(input())

sum_n = 0
max_n = -sys.maxsize

for _ in range(n):
    current_n = int(input())
    sum_n += current_n
    if current_n > max_n:
        max_n = current_n

remaining_n = sum_n - max_n

if max_n == remaining_n:
    print('Yes')
    print(f'Sum = {max_n}')
else:
    diff = abs(max_n - remaining_n)
    print('No')
    print(f'Diff = {diff}')
