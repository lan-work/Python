GOAL = 10000

steps_total = 0

while True:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        steps_total += steps_to_home
        break;

    steps = int(command)
    steps_total += steps

    if steps_total >= GOAL:
        break

diff = abs(steps_total - GOAL)

if steps_total >= GOAL:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')





