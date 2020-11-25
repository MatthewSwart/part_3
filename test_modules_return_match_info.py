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
