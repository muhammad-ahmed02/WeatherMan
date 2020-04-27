from getting_data import Data
from colorama import Fore, Style

chart_data = Data()


def chart(data, year, month):

    usable_year_month = []
    for item in data:
        if item[2] == int(year) and item[1] == month:
            usable_year_month.append(item)
    day = 0
    high_temp = 0
    low_temp = 0
    plot_high = 0
    plot_low = 0
    for sub_data in usable_year_month:
        day = sub_data[0]
        high_temp = sub_data[3]
        low_temp = sub_data[4]
        plot_high = '+'*high_temp
        plot_low = '+'*low_temp

    return f'Month: {month}th, Year: {year}\n{day} {Fore.RED}{plot_high}{Style.RESET_ALL} {high_temp}C\n{day} {Fore.BLUE}{plot_low}{Style.RESET_ALL} {low_temp}C'


question3 = chart(chart_data.data_chart(), 2011, 8)
print(question3)
