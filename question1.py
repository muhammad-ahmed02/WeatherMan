from getting_data import get_data_high, get_data_low, get_data_most_humid

data_high = get_data_high('C:/Users/shiek/PycharmProjects/Assignment1/weatherdata/')
data_low = get_data_low('C:/Users/shiek/PycharmProjects/Assignment1/weatherdata/')
data_humidity = get_data_most_humid('C:/Users/shiek/PycharmProjects/Assignment1/weatherdata/')

# To calculate highest temperature


def highest_temp(data, year):
    usable_year = []
    for item in data:
        if item[2] == int(year):
            usable_year.append(item)
    initial = 0
    day = 0
    month = ''
    for i in usable_year:
        if i[3] > initial:
            initial = i[3]
            day = i[0]
            month = i[1]

    return f'Highest: {initial}C on {month} {day}'


a = highest_temp(data_high, 2002)
print(a)

# To calculate lowest temperature


def lowest_temp(data, year):
    usable_year = []
    for item in data:
        if item[2] == int(year):
            usable_year.append(item)
    initial = 1000
    day = 0
    month = ''
    for i in usable_year:
        if initial > i[3]:
            initial = i[3]
            day = i[0]
            month = i[1]

    return f'Lowest: {initial}C on {month} {day}'


b = lowest_temp(data_low, 2002)
print(b)

# To calculate most humid day and humidity


def most_humid_day(data, year):
    usable_year = []
    for item in data:
        if item[2] == int(year):
            usable_year.append(item)
    initial = 0
    day = 0
    month = ''
    for i in usable_year:
        if i[3] > initial:
            initial = i[3]
            day = i[0]
            month = i[1]
    return f'Humid: {initial}% on {month} {day}'


c = most_humid_day(data_humidity, 2002)
print(c)
