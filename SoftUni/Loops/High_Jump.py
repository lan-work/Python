matches_won = 0
matches_lost = 0
overall_matches = 0

while True:
    tournament_name = input()

    if tournament_name == 'End of tournaments':
        break

    games_to_be_played = int(input())

    for i in range(1, games_to_be_played + 1):
        current_game_number = i
        overall_matches += 1
        desis_team_points = int(input())
        enemy_team_points = int(input())

        if desis_team_points > enemy_team_points:
            matches_won += 1
            print(f'Game {current_game_number} of tournament {tournament_name}: win with {desis_team_points - enemy_team_points} points.')
        else:
            matches_lost += 1
            print(f'Game {current_game_number} of tournament {tournament_name}: lost with {enemy_team_points - desis_team_points} points.')

win_rate = (matches_won / overall_matches) * 100
lose_rate = (matches_lost / overall_matches) * 100

print(f'{win_rate:.2f}% matches win')
print(f'{lose_rate:.2f}% matches lost')
