import sys

n = int(input())

min = sys.maxsize
max = -sys.maxsize

for _ in range(n):
    i = int(input())
    if i < min: min = i
    if i > max: max = i

print(f'Max number: {max}')
print(f'Min number: {min}')
