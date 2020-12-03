def parse_matches():
    """
    Read the full matches.csv file ignores first heading line breaks the data apart then adds the data to a list of
    lists called match_data and returns it.
    :return: match_data list
    """
    match_data = []
    with open('matches.csv') as matches:
        next(matches)
        for lines in matches:
            values = lines.strip().split(",")
            match_id = int(values[0])
            season = int(values[1])
            city = values[2]
            date = values[3]
            team_1 = values[4]
            team_2 = values[5]
            toss_winner = values[6]
            toss_decision = values[7]
            result = values[8]
            dl_applied = values[9]
            winner = values[10]
            win_by_runs = int(values[11])
            win_by_wicket = int(values[12])
            player_of_match = values[13]
            venue = values[14]
            umpire_1 = values[15]
            umpire_2 = values[16]
            field_data = [match_id, season, city, date, team_1, team_2, toss_winner, toss_decision, result, dl_applied,
                          winner,
                          win_by_runs, win_by_wicket, player_of_match, venue, umpire_1, umpire_2]
            match_data.append(field_data)
    return match_data


def parse_deliveries():

    delivery_data = []
    with open('deliveries.csv') as deliveries:
        next(deliveries)
        for lines in deliveries:
            values = lines.strip().split(",")
            match_id = int(values[0])
            inning = int(values[1])
            batting_team = values[2]
            bowling_team = values[3]
            over = int(values[4])
            ball = int(values[5])
            batsman = values[6]
            non_striker_batsman = values[7]
            bowler = values[8]
            is_super_over = int(values[9])
            wide_runs = int(values[10])
            bye_runs = int(values[11])
            legbye_runs = int(values[12])
            noball_runs = int(values[13])
            penalty_runs = int(values[14])
            batsman_runs = int(values[15])
            extra_runs = int(values[16])
            total_runs = int(values[17])
            player_dismissed = values[18]
            dismissal_kind = values[19]
            fielder = values[20]
            deliveries_data = [match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker_batsman,
                               bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs,
                               batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder]
            delivery_data.append(deliveries_data)
    return delivery_data


