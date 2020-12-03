from get_info import parse_matches as pm


def get_teams_in_year(year):
    """
    Searches through available data returned from modules_get_info function parse_matches for a given season.
    :param year: Between 2008 - 2017
    :return: Returns all teams playing in that season.
    """
    teams = []
    match_data = pm()
    for count in range(len(match_data)):
        if year == match_data[count][1]:
            if match_data[count][4] not in teams:
                teams.append(match_data[count][4])
            if match_data[count][5] not in teams:
                teams.append(match_data[count][5])

    return teams


