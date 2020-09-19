def is_uruu(year):
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)

def is_uruu2(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

for year in range(1950, 2051):
    if is_uruu2(year):
        print(year)

