n = int(input())

counter = 1
stop = False

for i in range(n):
    for j in range(i + 1):

        if counter > n:
            stop = True
            break

        print(counter, end=' ')
        counter += 1

    if stop:
        break

    print()
