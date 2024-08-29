import math

days_of_absence = int(input())
food_available = int(input())
food_daily_dog = float(input())
food_daily_cat = float(input())
food_daily_turtle = float(input())

food_consumed_dog = food_daily_dog * days_of_absence
food_consumed_cat = food_daily_cat * days_of_absence
food_consumed_turtle = (food_daily_turtle / 1000) * days_of_absence  # kilograms to grams
food_needed = food_consumed_dog + food_consumed_turtle + food_consumed_cat

diff = abs(food_available - food_needed)

if food_available >= food_needed:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')
