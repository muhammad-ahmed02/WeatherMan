from getting_data import get_data_chart
import os
import calendar
from colorama import Fore, Style

chart_data = get_data_chart(os.getcwd())


def chart(data, year, month):

    usable_year_month = []
    for item in data:
        if item[2] == int(year) and item[1] == calendar.month_name[month]:

            usable_year_month.append(item)
    print(f'Month: {month}, Year: {year}')
    for sub_data in usable_year_month:
        day = sub_data[0]
        high_temp = sub_data[3]
        low_temp = sub_data[4]

        plot_high = '+'*high_temp
        plot_low = '+'*low_temp

        print(f'{day} {Fore.RED}{plot_high}{Style.RESET_ALL} {high_temp}C')
        print(f'{day} {Fore.BLUE}{plot_low}{Style.RESET_ALL} {low_temp}C')


    return usable_year_month


a = chart(chart_data, 2002, 7)
