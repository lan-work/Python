BOX_SIZE = 1 * 1 * 1

width = int(input())
length = int(input())
height = int(input())

available_space = width * length * height
boxCapacity = int(available_space / BOX_SIZE)

while boxCapacity > 0:
    command = input()

    if command == 'Done':
        break

    boxes = int(command)
    boxCapacity -= boxes

if boxCapacity > 0:
    print(f'{boxCapacity} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(boxCapacity)} Cubic meters more.')
