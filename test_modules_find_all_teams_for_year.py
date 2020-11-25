from modules_find_all_teams_for_year import get_teams_in_year as gtiy

team_2008 = ['Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Chennai Super Kings', 'Kings XI Punjab',
             'Rajasthan Royals', 'Delhi Daredevils', 'Mumbai Indians', 'Deccan Chargers']
team_2009 = ['Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore', 'Rajasthan Royals',
             'Kings XI Punjab', 'Delhi Daredevils', 'Kolkata Knight Riders', 'Deccan Chargers']
team_2010 = ['Kolkata Knight Riders', 'Deccan Chargers', 'Mumbai Indians', 'Rajasthan Royals', 'Kings XI Punjab',
             'Delhi Daredevils', 'Royal Challengers Bangalore', 'Chennai Super Kings']
team_2011 = ['Chennai Super Kings', 'Kolkata Knight Riders', 'Deccan Chargers', 'Rajasthan Royals',
             'Kochi Tuskers Kerala', 'Royal Challengers Bangalore', 'Delhi Daredevils', 'Mumbai Indians',
             'Kings XI Punjab', 'Pune Warriors']
team_2012 = ['Chennai Super Kings', 'Mumbai Indians', 'Kolkata Knight Riders', 'Delhi Daredevils', 'Pune Warriors',
             'Rajasthan Royals', 'Kings XI Punjab', 'Royal Challengers Bangalore', 'Deccan Chargers']
team_2013 = ['Delhi Daredevils', 'Kolkata Knight Riders', 'Royal Challengers Bangalore', 'Mumbai Indians',
             'Sunrisers Hyderabad', 'Pune Warriors', 'Rajasthan Royals', 'Chennai Super Kings', 'Kings XI Punjab']
team_2014 = ['Kolkata Knight Riders', 'Mumbai Indians', 'Delhi Daredevils', 'Royal Challengers Bangalore',
             'Chennai Super Kings', 'Kings XI Punjab', 'Sunrisers Hyderabad', 'Rajasthan Royals']
team_2015 = ['Mumbai Indians', 'Kolkata Knight Riders', 'Chennai Super Kings', 'Delhi Daredevils', 'Rajasthan Royals',
             'Kings XI Punjab', 'Sunrisers Hyderabad', 'Royal Challengers Bangalore']
team_2016 = ['Mumbai Indians', 'Rising Pune Supergiants', 'Delhi Daredevils', 'Kolkata Knight Riders',
             'Kings XI Punjab', 'Gujarat Lions', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
team_2017 = ['Sunrisers Hyderabad', 'Royal Challengers Bangalore', 'Mumbai Indians', 'Rising Pune Supergiant',
             'Gujarat Lions', 'Kolkata Knight Riders', 'Kings XI Punjab', 'Delhi Daredevils']


def test_get_teams_in_year_len():
    """
    Assert the length of the value returned from get_teams_in_year. This data is checked against the numbers from the
    wikipedia pages listed below.

    2008 = https://en.wikipedia.org/wiki/2008_Indian_Premier_League#Teams_and_standings
    2009 = https://en.wikipedia.org/wiki/2009_Indian_Premier_League#Teams_and_standings
    2010 = https://en.wikipedia.org/wiki/2010_Indian_Premier_League#Teams_and_standings
    2011 = https://en.wikipedia.org/wiki/2011_Indian_Premier_League#Teams_and_standings
    2012 = https://en.wikipedia.org/wiki/2012_Indian_Premier_League#Teams_and_standings
    2013 = https://en.wikipedia.org/wiki/2013_Indian_Premier_League#Teams_and_standings
    2014 = https://en.wikipedia.org/wiki/2014_Indian_Premier_League#Teams_and_standings
    2015 = https://en.wikipedia.org/wiki/2015_Indian_Premier_League#Teams_and_standings
    2016 = https://en.wikipedia.org/wiki/2016_Indian_Premier_League#Teams_and_standings
    2017 = https://en.wikipedia.org/wiki/2017_Indian_Premier_League#Teams_and_standings
    """
    assert len(gtiy(2008)) == 8
    assert len(gtiy(2009)) == 8
    assert len(gtiy(2010)) == 8
    assert len(gtiy(2011)) == 10
    assert len(gtiy(2012)) == 9
    assert len(gtiy(2013)) == 9
    assert len(gtiy(2014)) == 8
    assert len(gtiy(2015)) == 8
    assert len(gtiy(2016)) == 8
    assert len(gtiy(2017)) == 8


def test_get_teams_in_year_names():
    """
    Test the team names of the value returned from get_teams_in_year. This data is checked against the numbers from
    the wikipedia pages listed below and is sorted to ensure they are the same.

    2008 = https://en.wikipedia.org/wiki/2008_Indian_Premier_League#Teams_and_standings
    2009 = https://en.wikipedia.org/wiki/2009_Indian_Premier_League#Teams_and_standings
    2010 = https://en.wikipedia.org/wiki/2010_Indian_Premier_League#Teams_and_standings
    2011 = https://en.wikipedia.org/wiki/2011_Indian_Premier_League#Teams_and_standings
    2012 = https://en.wikipedia.org/wiki/2012_Indian_Premier_League#Teams_and_standings
    2013 = https://en.wikipedia.org/wiki/2013_Indian_Premier_League#Teams_and_standings
    2014 = https://en.wikipedia.org/wiki/2014_Indian_Premier_League#Teams_and_standings
    2015 = https://en.wikipedia.org/wiki/2015_Indian_Premier_League#Teams_and_standings
    2016 = https://en.wikipedia.org/wiki/2016_Indian_Premier_League#Teams_and_standings
    2017 = https://en.wikipedia.org/wiki/2017_Indian_Premier_League#Teams_and_standings
    """
    assert sorted(gtiy(2008)) == sorted(team_2008)
    assert sorted(gtiy(2009)) == sorted(team_2009)
    assert sorted(gtiy(2010)) == sorted(team_2010)
    assert sorted(gtiy(2011)) == sorted(team_2011)
    assert sorted(gtiy(2012)) == sorted(team_2012)
    assert sorted(gtiy(2013)) == sorted(team_2013)
    assert sorted(gtiy(2014)) == sorted(team_2014)
    assert sorted(gtiy(2015)) == sorted(team_2015)
    assert sorted(gtiy(2016)) == sorted(team_2016)
    assert sorted(gtiy(2017)) == sorted(team_2017)
