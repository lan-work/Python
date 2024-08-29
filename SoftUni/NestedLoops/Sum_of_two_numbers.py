start = int(input())
end = int(input())
magic_number = int(input())

combinations_counter = 0
found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        combinations_counter += 1

        if i + j == magic_number:
            found = True
            break

    if found:
        break

if found:
    print(f'Combination N:{combinations_counter} ({i} + {j} = {magic_number})')
else:
    print(f'{combinations_counter} combinations - neither equals {magic_number}')
