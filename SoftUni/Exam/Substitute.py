n1d1_start = int(input())
n1d2_end = int(input())
n2d1_start = int(input())
n2d2_end = int(input())

n1d1_end = 8
n1d2_start = 9
n2d1_end = 8
n2d2_start = 9

changes_counter = 0
finish = False

for n1d1 in range(n1d1_start, n1d1_end + 1):
    if n1d1 % 2 != 0:
        continue

    for n1d2 in range(n1d2_start, n1d2_end - 1, -1):
        if n1d2 % 2 == 0:
            continue

        for n2d1 in range(n2d1_start, n2d1_end + 1):
            if n2d1 % 2 != 0:
                continue

            for n2d2 in range(n2d2_start, n2d2_end - 1, -1):
                if n2d2 % 2 == 0:
                    continue

                if n1d1 == n2d1 and n1d2 == n2d2:
                    print(f'Cannot change the same player.')
                    continue
                else:
                    changes_counter += 1
                    print(f'{n1d1}{n1d2} - {n2d1}{n2d2}')
                    if changes_counter == 6:
                        finish = True
                        break
            if finish:
                break
        if finish:
            break
    if finish:
        break
