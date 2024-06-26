pool_volume = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

liters_pipe1 = pipe1 * hours
liters_pipe2 = pipe2 * hours
liters_total = liters_pipe1 + liters_pipe2
filled_percentage = (liters_total / pool_volume) * 100

pipe1_percentage = (liters_pipe1 / liters_total) * 100
pipe2_percentage = (liters_pipe2 / liters_total) * 100

diff = abs(pool_volume - liters_total)
diff_percentage = (diff / pool_volume) * 100

overflow = True if (liters_total > pool_volume) else False

if overflow:
    print(f'For {hours} hours the pool overflows with {diff:.2f} liters.')
else:
    print(f'The pool is {filled_percentage:.2f}% full. '
          f'Pipe 1: {pipe1_percentage:.2f}%. Pipe 2: {pipe2_percentage:.2f}%.')
