GOAL = 10_000

steps_total = 0

while True:
    action = input()

    if action == 'Going home':
        steps_to_home = int(input())
        steps_total += steps_to_home
        break;

    steps = int(action)
    steps_total += steps

    if steps_total >= GOAL:
        break

diff = abs(steps_total - GOAL)

if steps_total >= GOAL:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')





