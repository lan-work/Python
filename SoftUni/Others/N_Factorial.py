n = int(input())
nfac = 1

while n > 0:
    nfac *= n
    n -= 1

print(nfac)