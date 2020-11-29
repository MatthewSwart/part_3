from modules_return_match_info import return_full_match_info as rfmi


def test_return_full_match_info():
    """
    Assert that the data returned is correct. Took 3 match ID's, counted the full two overs and counted the actual lines
    of data to ensure the correct data was coming back.
    """
    data_test_1 = rfmi(203)
    data_test_2 = rfmi(635)
    data_test_3 = rfmi(416)
    assert len(data_test_1) == 233
    assert len(data_test_2) == 242
    assert len(data_test_3) == 237


def test_return_full_match_info_types():
    """
    Assert that all the returned values within the list are of a specific type.
    """
    data_test_variable = rfmi(203)
    for lines in data_test_variable:
        assert type(lines[0]) is int
        assert type(lines[1]) is int
        assert type(lines[2]) is str
        assert type(lines[3]) is str
        assert type(lines[4]) is int
        assert type(lines[5]) is int
        assert type(lines[6]) is str
        assert type(lines[7]) is str
        assert type(lines[8]) is str
        assert type(lines[9]) is int
        assert type(lines[10]) is int
        assert type(lines[11]) is int
        assert type(lines[12]) is int
        assert type(lines[13]) is int
        assert type(lines[14]) is int
        assert type(lines[15]) is int
        assert type(lines[16]) is int
        assert type(lines[17]) is int
        assert type(lines[18]) is str
        assert type(lines[19]) is str
        assert type(lines[20]) is str
