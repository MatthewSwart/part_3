from return_all_match_data_from_year import all_match_data as amd
from return_match_info import return_full_match_info as rfmi

match_info = []
match_info_return = []
print('Welcome to IPL game data center\n')

while True:
    try:
        date = int(input('Please select a season between 2008 - 2017 (YYYY): '))
        if date in range(2008, 2018):
            match_info = amd(date)
            break
        else:
            print('\nIncorrect date or format please try again')
    except ValueError:
        print('Please only use a date between 2008 and 2017 and try again')

while True:
    try:
        input_game_id = int(input('Please select the Game ID for the match stats you would like: '))
        if input_game_id in range(len(match_info) + 1):
            match_id = match_info[(input_game_id - 1)][0]
            match_info_return = rfmi(match_id)
            break
        else:
            print(f'Please input a Game ID between 1 - {len(match_info)}')
    except ValueError:
        print(f'Incorrect please only use Game ID between 1 - {len(match_info)}')
