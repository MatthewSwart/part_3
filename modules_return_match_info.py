from modules_get_info import parse_deliveries as pds


def return_full_match_info(match_id):
    """

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
    data = return_full_match_info(203)
    print(len(data))