from modules_get_info import parse_matches as pm
from modules_get_info import parse_deliveries as pd


def test_parse_match():
    """
    Asserts that the input length is 636 which is the total matches.csv length.
    """
    assert len(pm()) == 636


def test_parse_deliveries():
    """
    Asserts that the input length is 150460 which is the total deliveries.csv file length
    """
    assert len(pd()) == 150460
