MOVIES_LIMIT = 7
limit_is_reached = False
best_movie = 0
highest_ascii = 0

for i in range(1, MOVIES_LIMIT + 1):

    command = input()
    if command == 'STOP':
        break

    limit_is_reached = True if i == MOVIES_LIMIT else False

    movie_title = command
    title_ascii_sum = 0

    for j in range(len(movie_title)):
        current_letter = movie_title[j]

        if current_letter.islower():
            title_ascii_sum -= len(movie_title) * 2
        elif current_letter.isupper():
            title_ascii_sum -= len(movie_title)

        title_ascii_sum += ord(current_letter)
        if title_ascii_sum > highest_ascii:
            best_movie = movie_title
            highest_ascii = title_ascii_sum

if limit_is_reached:
    print(f'The limit is reached.')

print(f'The best movie for you is {best_movie} with {highest_ascii} ASCII sum.')
