locations = int(input())

for i in range(locations):
    # STARTING A NEW LOCATION
    location_overall_yield = 0
    average_daily_yeild = 0

    expected_average_daily_yield = float(input())
    days_to_dig = int(input())

    for j in range(days_to_dig):
        daily_yield = float(input())

        location_overall_yield += daily_yield

    # LOCATION DONE
    average_daily_yeild = location_overall_yield / days_to_dig

    if average_daily_yeild >= expected_average_daily_yield:
        print(f'Good job! Average gold per day: {average_daily_yeild:.2f}.')
    else:
        print(f'You need {(expected_average_daily_yield - average_daily_yeild):.2f} gold.')
