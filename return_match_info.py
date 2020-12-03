from get_info import parse_deliveries as pds


def return_full_match_info(match_id):
    """
    This will return the complete game play for a specific match ID. A basic ball by ball play.
    Data information:
        match_id: ID that distinguishes between different games in the deliveries.csv file
        inning: Two innings in a game
        batting_team: Name of batting team
        bowling_team: Name of bowling team
        over: 20 overs in each innings, this number represents which over the innings is in.
        ball: 6 balls per over but this can be more with penalty balls
        batsman: Name of batsman facing the bowler
        non_striker: Name of batsman on opposite side of the crease
        bowler: Name of bowler
        is_super_over: Boolean value. Super over has to do with placement of fielders in the attempt to get batsmen to
                       hit as many 4's and 6's
        wide_runs: When a bowler bowls a wide a run is added to score
        bye_runs: Extra score if the batsman does not hit the ball or ball does not hit his body and the wicket keeper
                  does not catch the ball
        legbye_runs: Extra runs when ball doesn't touch the bat or batters hand.
        noball_runs: Extra run if bowler makes illegal delivery by stepping on or over popping crease or return crease
        penalty_runs: Extra runs as penalty runs for players' conduct
        batsman_runs: Actual runs hit by batsman
        extra_runs: Total of extra runs
        total_runs: Total of extra runs and batsman runs
        player_dismissed: Which batsman was dismissed
        dismissal_kind: Type of dismissal
        fielder: If a fielder played a part in it then their name will appear here.
    :param match_id:
    :return:
    """
    match_info = []
    match_data = pds()
    for line in match_data:
        if line[0] == match_id:
            match_info.append(line)
    return match_info


if __name__ == '__main__':
    data = return_full_match_info(416)
    print(data)
