floors = int(input())
rooms = int(input())
prefix = ''

for i in range(floors, 0, -1):
    for j in range(rooms):
        if i == floors:
            prefix = 'L'
        elif i % 2 == 0:
            prefix = 'O'
        else:
            prefix = 'A'
        print(f'{prefix}{i}{j}', end=' ')

    print()
