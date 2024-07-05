CHRYSANTHEMUMS_SUMMER = 2.00
ROSES_SUMMER = 4.10
TULIPS_SUMMER = 2.50
CHRYSANTHEMUMS_WINTER = 3.75
ROSES_WINTER = 4.50
TULIPS_WINTER = 4.15
HOLIDAYS_PRICES_PERCENTAGE = 0.15
BOUQUET_ARRANGEMENT = 2.00

chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

is_holiday = True if holiday == 'Y' else False
bouquet_total_price = 0.00

if season == 'Spring' or season == 'Summer':
    bouquet_total_price = (chrysanthemums * CHRYSANTHEMUMS_SUMMER + roses * ROSES_SUMMER + tulips * TULIPS_SUMMER)
else:
    bouquet_total_price = (chrysanthemums * CHRYSANTHEMUMS_WINTER + roses * ROSES_WINTER + tulips * TULIPS_WINTER)

if is_holiday:
    bouquet_total_price += (bouquet_total_price * HOLIDAYS_PRICES_PERCENTAGE)

if tulips > 7 and season == 'Spring':
    bouquet_total_price -= (bouquet_total_price * 0.05)
if roses > 10 and season == 'Winter':
    bouquet_total_price -= (bouquet_total_price * 0.10)
if (chrysanthemums + roses + tulips) > 20:
    bouquet_total_price -= (bouquet_total_price * 0.20)

bouquet_total_price += BOUQUET_ARRANGEMENT

print(f'{bouquet_total_price:.2f}')
