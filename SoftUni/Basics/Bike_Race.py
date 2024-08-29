JUNIORS_TRAIL_TAX = 5.50
JUNIORS_CROSS_COUNTRY_TAX = 8
JUNIORS_DOWNHILL_TAX = 12.25
JUNIORS_ROAD_TAX = 20
SENIORS_TRAIL_TAX = 7
SENIORS_CROSS_COUNTRY_TAX = 9.50
SENIORS_DOWNHILL_TAX = 13.75
SENIORS_ROAD_TAX = 21.50

EXPENSES_PERCENTAGE = 0.05
CROSS_COUNTRY_DISCOUNT_PERCENTAGE = 0.25

junior_bikers = int(input())
senior_bikers = int(input())
trace_type = input()

if trace_type == 'trail':
    total_sum = junior_bikers * JUNIORS_TRAIL_TAX + senior_bikers * SENIORS_TRAIL_TAX
elif trace_type == 'cross-country':
    total_sum = junior_bikers * JUNIORS_CROSS_COUNTRY_TAX + senior_bikers * SENIORS_CROSS_COUNTRY_TAX
elif trace_type == 'downhill':
    total_sum = junior_bikers * JUNIORS_DOWNHILL_TAX + senior_bikers * SENIORS_DOWNHILL_TAX
elif trace_type == 'road':
    total_sum = junior_bikers * JUNIORS_ROAD_TAX + senior_bikers * SENIORS_ROAD_TAX

total_sum -= (total_sum * EXPENSES_PERCENTAGE)

if (junior_bikers + senior_bikers) >= 50 and trace_type == 'cross-country':
    total_sum -= (total_sum * CROSS_COUNTRY_DISCOUNT_PERCENTAGE)

print(f'{total_sum:.2f}')
