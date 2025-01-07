def is_year_leap(year):
    if year < 1582:
        return False
    else:
        if year%4 != 0:
            return False
        elif year%100 != 0:
            return True
        elif year%400 != 0:
            return False
        else:
            return True


def days_in_month(year, month):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29
        return days[month-1]
    return days[month-1]


def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None
    
    


print(day_of_year(2000, 12, 31))
