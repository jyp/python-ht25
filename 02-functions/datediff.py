# Problem: how old am i (in number of days)?

# generalisation: what is the number of days between two arbitrary dates ?
# (in the Gregorian calendar)


# input: two dates (three integers each)
# output: the number (int)

# approximate:
average_number_of_days_in_a_year = 365.2422
average_number_of_days_in_a_month =  average_number_of_days_in_a_year / 12
def date_diff_approx(y1,m1,d1 , y2,m2,d2):
    return ((y2-y1)*average_number_of_days_in_a_year
            + (m2-m1)*average_number_of_days_in_a_month
            + (d2-d1))

# Every year that is exactly divisible by four is a leap year, except
# for years that are exactly divisible by 100, but these centurial
# years are leap years if they are exactly divisible by 400. For
# example, the years 1700, 1800, and 1900 are not leap years, but the
# years 1600 and 2000 are.

def is_divisible_by(n,x):
    return x % n == 0

def is_leap_year(y):
    return (is_divisible_by(4,y) and not is_divisible_by(100,y)) or is_divisible_by(400,y)

assert (not is_leap_year(2025))
assert (is_leap_year(2020))
assert (not is_leap_year(1700))
assert (is_leap_year(2000))

def number_of_days_in_year(y):
    if is_leap_year(y):
        return 366
    else:
        return 365

def number_of_days_in_month(y,m):
    if m==2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    elif m in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

def days_since_epoch(date):
    (y,m,d) = date
    result = 0
    for year in range(1,y):
        result = result + number_of_days_in_year(year)
    for month in range(1,m):
        result = result + number_of_days_in_month(y,month)
    result = result + d
    return result

def date_diff(date1 , date2):
    return days_since_epoch(date2) - days_since_epoch(date1)


# 


print(date_diff ((1978,12,15), (2025,9,4)))
print("some tests")
print(date_diff ((2024,9,4), (2025,9,4)))
print(date_diff ((2025,9,4), (2025,9,4)))
print(date_diff ((2025,9,2), (2025,9,4)))
print(date_diff ((2024,9,4), (2025,9,4)))
# print(date_diff_approx (1978,12,15, 2025,9,4))
