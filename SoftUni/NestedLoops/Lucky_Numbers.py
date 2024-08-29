n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if k > i + j:
                break

            for l in range(1, 10):
                if l > i + j:
                    break

                if i + j == k + l:
                    if n % (i + j) == 0:
                        print(f'{i}{j}{k}{l}', end=' ')
