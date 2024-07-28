start = input()
end = input()
skip = input()

start = ord(start)
end = ord(end)
skip = ord(skip)

combinations = 0

for i in range(start, end + 1):
    if i == skip:
        continue

    for j in range(start, end + 1):
        if j == skip:
            continue

        for k in range(start, end + 1):
            if k == skip:
                continue

            print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
            combinations += 1

print(combinations)
