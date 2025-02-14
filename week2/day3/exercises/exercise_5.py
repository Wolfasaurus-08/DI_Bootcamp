from datetime import datetime

def time_until_new_year():
    now = datetime.now()
    current_year = now.year

    new_year_str = f'{current_year + 1}-01-01 00:00:00'

    new_year = datetime.strptime(new_year_str, '%Y-%m-%d %H:%M:%S')

    time_difference = new_year - now

    days = time_difference.days
    seconds = time_difference.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'The 1st of January is in {days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours.'

time_left = time_until_new_year()
print(time_left)