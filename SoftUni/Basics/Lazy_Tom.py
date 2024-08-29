import math

area = int(input())
harvest = float(input())
wine_needed = int(input())
workers_count = int(input())

grapes_for_wine = (harvest * area) * 0.4
wine_produced = grapes_for_wine / 2.5
diff = abs(wine_produced - wine_needed)

if wine_produced < wine_needed:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(diff / workers_count)} liters per person.')
