FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

tabs_opened = int(input())
salary = int(input())

for _ in range(tabs_opened):
    website = input()
    if website == 'Facebook':
        salary -= FACEBOOK_FINE
    elif website == 'Instagram':
        salary -= INSTAGRAM_FINE
    elif website == 'Reddit':
        salary -= REDDIT_FINE

    if not salary:
        print('You have lost your salary.')
        break
else:
    print(salary)
