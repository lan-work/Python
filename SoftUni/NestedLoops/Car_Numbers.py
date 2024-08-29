start = int(input())
end = int(input())

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for l in range(start, end + 1):
                if (j + k) % 2 != 0:
                    continue
                if i % 2 == 0 and l % 2 == 0:
                    continue
                if i % 2 != 0 and l % 2 != 0:
                    continue
                if not (i > l):
                    continue
                print(f'{i}{j}{k}{l}', end=' ')
