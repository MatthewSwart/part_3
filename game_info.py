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

    for value in ball_dict.values():
        if value.get('batsman', False) not in bat_team_1 and value.get('inning', False) == 1:
            bat_team_1.append(value.get('batsman', False))
        if value.get('batsman', False) not in bat_team_2 and value.get('inning', False) == 2:
            bat_team_2.append(value.get('batsman', False))

    runs_team_1 = [[] for i in range(len(bat_team_1))]
    runs_team_2 = [[] for i in range(len(bat_team_1))]

    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bat_team_1.index(value.get('batsman', False))
            runs_team_1[position].append(value.get('total_runs', False))
        if value.get('inning', False) == 2:
            position = bat_team_2.index(value.get('batsman', False))
            runs_team_2[position].append(value.get('total_runs', False))

    batsman_list.append(bat_team_1)
    batsman_list.append(runs_team_1)
    print(sum(runs_team_1))
    batsman_list.append(bat_team_2)
    batsman_list.append(runs_team_2)

    return batsman_list


def bowler_stats(ball_dict):
    """
    Bowler statistics are very vast for each game. This takes all the stats for bowlers and adds them to lists. This
    can be used from the menu to either acquire a bowlers stats from a single game or as part of the analysis for the
    full season.
    :param ball_dict: Comes in from return_full_match_info.
    :return: bowler_list
    """
    bowler_dict = {}
    team_list = []
    for value in ball_dict.values():
        if value.get('batting_team') not in bowler_dict:
            bowler_dict[value.get('batting_team')] = {}
            team_list.append(value.get('batting_team'))
    bowler_team_2 = []
    bowler_team_1 = []
    for value in ball_dict.values():
        if value.get('bowler', False) not in bowler_team_2 and value.get('inning', False) == 1:
            bowler_team_2.append(value.get('bowler', False))
        if value.get('bowler', False) not in bowler_team_1 and value.get('inning', False) == 2:
            bowler_team_1.append(value.get('bowler', False))
    for inputs in bowler_team_1:
        bowler_dict[team_list[0]][inputs] = {}
    for inputs in bowler_team_2:
        bowler_dict[team_list[1]][inputs] = {}

    wide_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    wide_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            wide_runs_bowler_team_2[position].append(value.get('wide_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            wide_runs_bowler_team_1[position].append(value.get('wide_runs', False))

    bye_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    bye_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            bye_runs_bowler_team_2[position].append(value.get('bye_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            bye_runs_bowler_team_1[position].append(value.get('bye_runs', False))

    legbye_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    legbye_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            legbye_runs_bowler_team_2[position].append(value.get('legbye_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            legbye_runs_bowler_team_1[position].append(value.get('legbye_runs', False))

    noball_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    noball_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            noball_runs_bowler_team_2[position].append(value.get('noball_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            noball_runs_bowler_team_1[position].append(value.get('noball_runs', False))

    penalty_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    penalty_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            penalty_runs_bowler_team_2[position].append(value.get('penalty_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            penalty_runs_bowler_team_1[position].append(value.get('penalty_runs', False))

    batsman_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    batsman_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            batsman_runs_bowler_team_2[position].append(value.get('batsman_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            batsman_runs_bowler_team_1[position].append(value.get('batsman_runs', False))

    extra_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    extra_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            position = bowler_team_2.index(value.get('bowler', False))
            extra_runs_bowler_team_2[position].append(value.get('extra_runs', False))
        if value.get('inning', False) == 2:
            position = bowler_team_1.index(value.get('bowler', False))
            extra_runs_bowler_team_1[position].append(value.get('extra_runs', False))

    player_dismissed_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    player_dismissed_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            if not value.get('player_dismissed'):
                continue
            else:
                if not value.get('fielder'):
                    position = bowler_team_2.index(value.get('bowler', False))
                    player_dismissed_bowler_team_2[position].append(value.get('player_dismissed', False))
        if value.get('inning', False) == 2:
            if not value.get('player_dismissed'):
                continue
            else:
                if not value.get('fielder'):
                    position = bowler_team_1.index(value.get('bowler', False))
                    player_dismissed_bowler_team_1[position].append(value.get('player_dismissed', False))

    dismissal_kind_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    dismissal_kind_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    for value in ball_dict.values():
        if value.get('inning', False) == 1:
            if not value.get('player_dismissed'):
                continue
            else:
                if not value.get('fielder'):
                    position = bowler_team_2.index(value.get('bowler', False))
                    dismissal_kind_bowler_team_2[position].append(value.get('dismissal_kind', False))
        if value.get('inning', False) == 2:
            if not value.get('player_dismissed'):
                continue
            else:
                if not value.get('fielder'):
                    position = bowler_team_1.index(value.get('bowler', False))
                    dismissal_kind_bowler_team_1[position].append(value.get('dismissal_kind', False))

    for count in range(len(bowler_team_1)):
        bowler_dict[team_list[0]][bowler_team_1[count]]['wide_runs'] = sum(wide_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['bye_runs'] = sum(bye_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['legbye_runs'] = sum(legbye_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['noball_runs'] = sum(noball_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['penalty_runs'] = sum(penalty_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['batsman_runs'] = sum(batsman_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['extra_runs'] = sum(extra_runs_bowler_team_1[count])
        bowler_dict[team_list[0]][bowler_team_1[count]]['player_dismissed'] = player_dismissed_bowler_team_1[count]
        bowler_dict[team_list[0]][bowler_team_1[count]]['dismissal_kind'] = dismissal_kind_bowler_team_1[count]

    for count in range(len(bowler_team_2)):
        bowler_dict[team_list[1]][bowler_team_2[count]]['wide_runs'] = sum(wide_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['bye_runs'] = sum(bye_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['legbye_runs'] = sum(legbye_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['noball_runs'] = sum(noball_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['penalty_runs'] = sum(penalty_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['batsman_runs'] = sum(batsman_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['extra_runs'] = sum(extra_runs_bowler_team_2[count])
        bowler_dict[team_list[1]][bowler_team_2[count]]['player_dismissed'] = player_dismissed_bowler_team_2[count]
        bowler_dict[team_list[1]][bowler_team_2[count]]['dismissal_kind'] = dismissal_kind_bowler_team_2[count]





