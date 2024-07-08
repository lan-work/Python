user_num = int(input())

for special_num in range(1111, 9999 + 1):
    is_special = True

    # SAME AS enumerate()
    # special_string = str(special_num)
    # for s in special_string:
    #     n = int(s)
    #     if n == 0 or user_num % n != 0:
    #         is_special = False
    #         break

    for index, digit in enumerate(str(special_num)):
        if int(digit) == 0 or user_num % int(digit) != 0:
            is_special = False
            break

    if is_special:
        print(special_num, end=' ')
