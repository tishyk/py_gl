from datetime import datetime


def is_weekday():
    """ Python's datetime library treats Monday as 0 and Sunday as 6"""
    day = datetime.today()

    print(day)
    return 0 <= day.weekday() < 5

# Test if today is a weekday
# assert is_weekday()
# print(is_weekday())
