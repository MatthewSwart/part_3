from return_match_info import return_full_match_info as rfmi


def sort_match_data(match_id):
    """
    This breaks up all the information for one game in a specific season on a specific day. This is then added to a
    dictionary of dictionaries.

    Dictionary key list:
        match_id: int,
        inning: int,
        batting_team: string,
        bowling_team: string,
        over: int,
        ball: int,
        batsman: string,
        non_striker: string,
        bowler: string,
        is_super_over: int,
        wide_runs: int,
        bye_runs: int,
        legbye_runs: int,
        noball_runs: int,
        penalty_runs: int,
        batsman_runs: int,
        extra_runs: int,
        total_runs: int,
        player_dismissed: string,
        dismissal_kind: string,
        fielder: string,
    :param match_id: Comes in from return_full_match_info.
    :return: ball_dict - Data in dictionary format for each ball of each innings.
    """
    count = 0
    ball_dict = {}
    full_match_data = rfmi(match_id)
    for line in full_match_data:
        match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, \
        wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, \
        player_dismissed, dismissal_kind, fielder = line
        build_dict_name = f'inning_{inning}over_{over}_ball_{ball}'
        ball_dict[build_dict_name] = {}
        ball_dict[build_dict_name]['match_id'] = int(match_id)
        ball_dict[build_dict_name]['inning'] = int(inning)
        ball_dict[build_dict_name]['batting_team'] = batting_team
        ball_dict[build_dict_name]['bowling_team'] = bowling_team
        ball_dict[build_dict_name]['over'] = int(over)
        ball_dict[build_dict_name]['ball'] = int(ball)
        ball_dict[build_dict_name]['batsman'] = batsman
        ball_dict[build_dict_name]['non_striker'] = non_striker
        ball_dict[build_dict_name]['bowler'] = bowler
        ball_dict[build_dict_name]['is_super_over'] = int(is_super_over)
        ball_dict[build_dict_name]['wide_runs'] = int(wide_runs)
        ball_dict[build_dict_name]['bye_runs'] = int(bye_runs)
        ball_dict[build_dict_name]['legbye_runs'] = int(legbye_runs)
        ball_dict[build_dict_name]['noball_runs'] = int(noball_runs)
        ball_dict[build_dict_name]['penalty_runs'] = int(penalty_runs)
        ball_dict[build_dict_name]['batsman_runs'] = int(batsman_runs)
        ball_dict[build_dict_name]['extra_runs'] = int(extra_runs)
        ball_dict[build_dict_name]['total_runs'] = int(total_runs)
        ball_dict[build_dict_name]['player_dismissed'] = player_dismissed
        ball_dict[build_dict_name]['dismissal_kind'] = dismissal_kind
        ball_dict[build_dict_name]['fielder'] = fielder
    return ball_dict


def batsmen_stats(ball_dict):
    """
    Uses the information returned from sort_match_data to get the batsman stats for visualisation. 4 list are created
    2 containing batsmen names from each innings and 2 containing their ball by ball score.
    :param ball_dict: Information returned from sort_match_data
    :return: batsman_list - list of lists
    """
    batsman_list = []
    bat_team_1 = []
    bat_team_2 = []

    for values in ball_dict.values():
        if values.get('batsman', False) not in bat_team_1 and values.get('inning', False) == 1:
            bat_team_1.append(values.get('batsman', False))
        if values.get('batsman', False) not in bat_team_2 and values.get('inning', False) == 2:
            bat_team_2.append(values.get('batsman', False))
    runs_team_1 = [[]] * len(bat_team_1)
    runs_team_2 = [[]] * len(bat_team_2)
    for values in ball_dict.values():
        if values.get('inning', False) == 1:
            position = bat_team_1.index(values.get('batsman', False))
            runs_team_1[position].append(values.get('total_runs', False))
        if values.get('inning', False) == 2:
            position = bat_team_2.index(values.get('batsman', False))
            runs_team_2[position].append(values.get('total_runs', False))
    batsman_list.append(bat_team_1)
    batsman_list.append(runs_team_1)
    batsman_list.append(bat_team_2)
    batsman_list.append(runs_team_2)
    return batsman_list


if __name__ == '__main__':
    dict_balls = sort_match_data(413)
#    for entries in dict_balls:
#       print(entries)
#    for fielder in dict_balls.values():
#        if fielder.get('fielder', False) != '':
#            print(fielder.get('fielder'))
    batsmen_stats(dict_balls)
