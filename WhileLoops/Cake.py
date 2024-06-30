SLICE_SIZE = 1 * 1

cake_width = int(input())
cake_length = int(input())

slices_left = int((cake_width * cake_length) / SLICE_SIZE)

while slices_left > 0:
    command = input()

    if command == 'STOP':
        break

    cake_slice = int(command)
    slices_left -= cake_slice

if command == 'STOP':
    print(f'{slices_left} pieces are left.')
else:
    print(f'No more cake left! You need {abs(slices_left)} pieces more.')
