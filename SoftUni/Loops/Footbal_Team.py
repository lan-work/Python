team_name = input()
matches_played = int(input())

score = 0
wins = 0
draws = 0
loses = 0

if matches_played == 0:
    print(f'{team_name} hasn\'t played any games during this season.')
else:
    for i in range(matches_played):

        result = input()

        if result == 'W':
            wins += 1
            score += 3
        elif result == 'D':
            draws += 1
            score += 1
        elif result == 'L':
            loses += 1
            continue

    win_rate = (wins / matches_played) * 100
    print(f'{team_name} has won {score} points during this season.')
    print('Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {loses}')
    print(f'Win rate: {win_rate:.2f}%')
