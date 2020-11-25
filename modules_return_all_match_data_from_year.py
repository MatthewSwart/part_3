from modules_get_info import parse_matches as pm


def all_match_data(year):
    """
    Searches through the parse_matches data for all games in a specific season prints them out with a game ID and
    returns the data in a list to the main program
    :param year: Specific format YYYY between 2008 - 2017
    :return: year_match_data
    """
    year_match_data = []
    match_year_data = pm()
    for count in range(len(match_year_data)):
        if year == match_year_data[count][1]:
            year_match_data.append(match_year_data[count])
    for count in range(len(year_match_data)):
        print(
            f'Game ID: {count + 1} Match date: {year_match_data[count][3]} {year_match_data[count][4]} vs '
            f'{year_match_data[count][5]}')

    return year_match_data


if __name__ == '__main__':
    data = all_match_data(2017)
    print(data[3])
