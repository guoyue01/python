def year(year):
    if year%400 == 0:
        return 1
    elif year%100 != 0 and year%4 == 0:
        return 1
    else:
        return 0