from modules_find_all_teams_for_year import get_teams_in_year as gtiy

start_date = 2008
print('Available season dates:')
for count in range(1, 11):
    if count >= 10:
        print(f'{count}: {start_date}')
    else:
        print(f' {count}: {start_date}')
    start_date += 1
date = int(input('Please input the required date (YYYY): '))
teams = []
if (date >= 2008) and (date <= 2017):
    teams = gtiy(date)
else:
    print('Incorrect selection')

for lines in teams:
    print(lines)
