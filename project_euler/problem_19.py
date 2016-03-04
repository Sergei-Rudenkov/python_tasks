import itertools

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# https://projecteuler.net/problem=19


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months_map = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
              'September': 30, 'October': 31, 'November': 30, 'December': 31}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']


def week_generator():
    for day in itertools.cycle(days):
        yield day


def month_generator():
    for month in itertools.cycle(months):
        yield month


mg = month_generator()
wg = week_generator()


def main():
    count = 0
    year = 1900
    last_month_day = wg.next()
    while year < 2001:
        leap_year = False
        month = mg.next()
        if month == 'January':
            year += 1
        if year % 4 == 0:
            leap_year = True
        for _ in range(months_map[month]):
            last_month_day = wg.next()
        if month == 'February' and leap_year:
            last_month_day = wg.next()
        if last_month_day == 'Saturday':
            count += 1
    print "%s Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)" % count


if __name__ == "__main__":
    main()
