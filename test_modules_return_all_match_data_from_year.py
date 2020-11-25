from modules_return_all_match_data_from_year import all_match_data as amd


def test_all_match_data():
    """
    Assert the length of the value returned from all_match_data. This data is checked against the numbers from the
    wikipedia pages listed below.

    2008 = https://en.wikipedia.org/wiki/2008_Indian_Premier_League#League_stage
    2009 = https://en.wikipedia.org/wiki/2009_Indian_Premier_League#League_stage
    2010 = https://en.wikipedia.org/wiki/2010_Indian_Premier_League#League_stage
    2011 = https://en.wikipedia.org/wiki/2011_Indian_Premier_League#League_stage
    2012 = https://en.wikipedia.org/wiki/2012_Indian_Premier_League#League_stage
    2013 = https://en.wikipedia.org/wiki/2013_Indian_Premier_League#League_stage
    2014 = https://en.wikipedia.org/wiki/2014_Indian_Premier_League#League_stage
    2015 = https://en.wikipedia.org/wiki/2015_Indian_Premier_League#League_stage
    2016 = https://en.wikipedia.org/wiki/2016_Indian_Premier_League#League_stage
    2017 = https://en.wikipedia.org/wiki/2017_Indian_Premier_League#League_stage
    """
    assert len(amd(2008)) == 58
    assert len(amd(2009)) == 57
    assert len(amd(2010)) == 60
    assert len(amd(2011)) == 73
    assert len(amd(2012)) == 74
    assert len(amd(2013)) == 76
    assert len(amd(2014)) == 60
    assert len(amd(2015)) == 59
    assert len(amd(2016)) == 60
    assert len(amd(2017)) == 59


match_data_2008_50 = [110, 2008, 'Chennai', '24/05/2008', 'Rajasthan Royals', 'Chennai Super Kings', 'Rajasthan Royals',
                      'bat', 'normal', '0', 'Rajasthan Royals', 10, 0, 'JA Morkel', 'MA Chidambaram Stadium Chepauk',
                      'DJ Harper', 'SL Shastri']
match_data_2017_3 = [4, 2017, 'Indore', '08/04/2017', 'Rising Pune Supergiant', 'Kings XI Punjab', 'Kings XI Punjab',
                     'field', 'normal', '0', 'Kings XI Punjab', 0, 6, 'GJ Maxwell', 'Holkar Cricket Stadium',
                     'AK Chaudhary', 'C Shamshuddin']


def test_all_match_data_output_list():
    """
    Assert data from all_match_data is correct . This data is checked against the numbers from the
    wikipedia pages listed below.

    2008 = https://en.wikipedia.org/wiki/2008_Indian_Premier_League#League_stage
    2017 = https://en.wikipedia.org/wiki/2017_Indian_Premier_League#League_stage
    """
    data_test = amd(2008)
    assert data_test[50] == match_data_2008_50
    data_test = amd(2017)
    assert data_test[3] == match_data_2017_3
