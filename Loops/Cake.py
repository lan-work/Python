SLICE_SIZE = 1 * 1

cake_width = int(input())
cake_length = int(input())

slices_left = int((cake_width * cake_length) / SLICE_SIZE)

while slices_left > 0:
    action = input()

    if action == 'STOP':
        result = f'{slices_left} pieces are left.'
        break

    slices_taken = int(action)
    slices_left -= slices_taken
else:
    result = f'No more cake left! You need {abs(slices_left)} pieces more.'

print(result)
