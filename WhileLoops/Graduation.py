MAX_GRADUATION_YEAR = 12
MAX_FAIL_ATTEPMTS = 2

student_name = input()
current_year = 1
failures = 0
total_grades = 0

while current_year <= MAX_GRADUATION_YEAR:
    grade = float(input())

    if grade >= 4:
        total_grades += grade
        current_year += 1
    else:
        failures += 1
        if failures >= MAX_FAIL_ATTEPMTS:
            print(f'{student_name} has been excluded at {current_year} grade')
            break
else:
    average_grade = total_grades / (current_year - 1)
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
