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
    batsman_list.append(bat_team_2)
    batsman_list.append(runs_team_2)

    return batsman_list

def bowler_stats(ball_dict):
    bowler_list =[]
    bowler_team_2 = []
    bowler_team_1 = []

    for value in ball_dict.values():
        if value.get('bowler', False) not in bowler_team_2 and value.get('inning', False) == 1:
            bowler_team_2.append(value.get('bowler', False))
        if value.get('bowler', False) not in bowler_team_1 and value.get('inning', False) == 2:
            bowler_team_1.append(value.get('bowler', False))
    wide_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    wide_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    bye_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    bye_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    legbye_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    legbye_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    noball_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    noball_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    penalty_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    penalty_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    batsman_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    batsman_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    extra_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    extra_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]
    total_runs_bowler_team_2 = [[] for i in range(len(bowler_team_2))]
    total_runs_bowler_team_1 = [[] for i in range(len(bowler_team_1))]



if __name__ == '__main__':
    dict_balls = sort_match_data(413)
#    for entries in dict_balls:
#       print(entries)
#    for fielder in dict_balls.values():
#        if fielder.get('fielder', False) != '':
#            print(fielder.get('fielder'))
    data = batsmen_stats(dict_balls)
    for count in range(len(data[0])):
        print(data[1][count])
    for count in range(len(data[0])):
        print("{:<15} : {:<1}".format(data[0][count], sum(data[1][count])))
