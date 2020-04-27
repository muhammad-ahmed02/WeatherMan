from getting_data import Data

main_data = Data()


def temperatures(data, year):
    usable_year = []
    for item in data:
        if item[2] == int(year):
            usable_year.append(item)
    h_temp = 0
    l_temp = 1000
    max_humid = 0
    h_temp_day = 0
    l_temp_day = 0
    max_humid_day = 0
    h_temp_month = 0
    l_temp_month = 0
    max_humid_month = 0
    for i in usable_year:
        if i[3] > h_temp:
            h_temp = i[3]
            h_temp_day = i[0]
            h_temp_month = i[1]

        if i[4] < l_temp:
            l_temp = i[4]
            l_temp_day = i[0]
            l_temp_month = i[1]

        if i[5] > max_humid:
            max_humid = i[5]
            max_humid_day = i[0]
            max_humid_month = i[1]

    return f'Highest: {h_temp}C on {h_temp_day}/{h_temp_month}\nLowest: {l_temp}C on {l_temp_day}/{l_temp_month}\nHumid: {max_humid}% on {max_humid_day}/{max_humid_month}'


question1 = temperatures(main_data.get_data_temp(), 2011)
print(question1)