start_x = 1
end_x = int(input())

start_y = 1
end_y = int(input())

passwords_needed = int(input())

start_a = 35
max_a = 55

start_b = 64
max_b = 96

a = start_a
b = start_b

passwords_done = False
passwords_generated = 0

for x in range(start_x, end_x + 1):
    for y in range(start_y, end_y + 1):

        if a > max_a:
            a = start_a

        if b > max_b:
            b = start_b

        passwords_generated += 1
        print(f'{chr(a)}{chr(b)}{x}{y}{chr(b)}{chr(a)}', end='|')

        a += 1
        b += 1

        if passwords_generated >= passwords_needed:
            passwords_done = True
            break
    if passwords_done:
        break
