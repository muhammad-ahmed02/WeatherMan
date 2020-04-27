from getting_data import Data
from statistics import mean

average_data = Data()


def average(data, year, month):
    usable_year_month = []
    for item in data:
        if item[2] == int(year) and item[1] == month:
            usable_year_month.append(item)
    max_temp = 0
    low_temp = 0
    mean_humid = 0
    for i in usable_year_month:
        if i[3] > max_temp and i[4] > low_temp and i[5] > mean_humid:
            max_temp = i[3]
            low_temp = i[4]
            mean_humid = i[5]
    new_max_temp = []
    new_min_temp = []
    new_mean_humid = []
    for items in usable_year_month:
        new_max_temp.append(items[3])
        new_min_temp.append(items[4])
        new_mean_humid.append(items[5])
    mean_max_temp = int(mean(new_max_temp))
    mean_min_temp = int(mean(new_min_temp))
    mean_mean_humid = int(mean(new_mean_humid))

    return f'Highest Average: {mean_max_temp}C \nLowest Average: {mean_min_temp}C \nAverage Humidity: {mean_mean_humid}%'


question2 = average(average_data.data_average(), 2005, 6)
print(question2)
