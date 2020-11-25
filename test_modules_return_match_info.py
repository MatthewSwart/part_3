from modules_return_match_info import f


def test_full_match_info():
    output_data = fmi(203)
    assert len(output_data) == 233
