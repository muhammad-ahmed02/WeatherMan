import csv
import os

os.chdir('C:/Users/shiek/PycharmProjects/Assignment1/weatherdata/')


def get_data_high(directory):

    max_temp = []
    month = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    for dir, subdir, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                with open(os.path.join(directory, filename), 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:
                        # one list of temperature and dates
                        temp_dates = []
                        # list of temperature
                        temp = line[1:2]
                        # list of dates
                        date = line[0:1]
                        if len(temp) >= 1:
                            try:
                                # adding day in list.
                                temp_dates.append(int(date[0].split('-')[-1]))
                                # adding month in list.
                                temp_dates.append(month[str(int(date[0].split('-')[-2]))])
                                # adding year in list.
                                temp_dates.append(int(date[0].split('-')[-3]))
                                # adding temperature in list.
                                temp_dates.append(int(temp[0]))
                            except ValueError:
                                pass
                        # verifying data in main list.
                        if len(temp_dates) == 4:
                            max_temp.append(temp_dates)
    return max_temp


def get_data_low(directory):
    min_temp = []
    month = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    for dir, subdir, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                with open(os.path.join(directory, filename), 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:
                        # one list of temperature and dates
                        temp_dates = []
                        # list of temperature
                        temp = line[3:4]
                        # list of dates
                        date = line[0:1]
                        if len(temp) >= 1:
                            try:
                                # adding day in list.
                                temp_dates.append(int(date[0].split('-')[-1]))
                                # adding month in list.
                                temp_dates.append(month[str(int(date[0].split('-')[-2]))])
                                # adding year in list.
                                temp_dates.append(int(date[0].split('-')[-3]))
                                # adding temperature in list.
                                temp_dates.append(int(temp[0]))
                            except ValueError:
                                pass
                        # verifying data in main list.
                        if len(temp_dates) == 4:
                            min_temp.append(temp_dates)
    return min_temp


def get_data_most_humid(directory):

    max_humid = []
    for dir, subdir, filenames in os.walk(os.getcwd()):

        month = {
            '1': 'Jan',
            '2': 'Feb',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                with open(os.path.join(os.getcwd(), filename), 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:
                        # one list of Max humidity and dates
                        humid_dates = []
                        # list of Max Humidities
                        max_humidity = line[7:8]
                        # list of dates
                        date = line[0:1]
                        if len(max_humidity) >= 1:
                            try:
                                # adding day in list.
                                humid_dates.append(int(date[0].split('-')[-1]))
                                # adding month in list.
                                humid_dates.append(month[str(int(date[0].split('-')[-2]))])
                                # adding year in list.
                                humid_dates.append(int(date[0].split('-')[-3]))
                                # adding temperature in list.
                                humid_dates.append(int(max_humidity[0]))
                            except ValueError:
                                pass
                        if len(humid_dates) == 4:
                            max_humid.append(humid_dates)
    return max_humid


def get_data_average(directory):
    max_temp = []
    month = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    for dir, subdir, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                with open(os.path.join(directory, filename), 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:
                        # one list containing highest temperature, lowest temperature, humidity.
                        all_values = []
                        # list of Max Temperature
                        high_temp = line[1:2]
                        # list of Min Temperature
                        low_temp = line[3:4]
                        # list of Mean Humidity
                        mean_humidity = line[8:9]
                        # list of dates
                        date = line[0:1]
                        # removing all empty objects from list.
                        if len(high_temp) >= 1 and len(low_temp) >= 1 and len(mean_humidity) >= 1:
                            try:
                                # adding day in list.
                                all_values.append(int(date[0].split('-')[-1]))
                                # adding month in list.
                                all_values.append(month[str(int(date[0].split('-')[-2]))])
                                # adding year in list.
                                all_values.append(int(date[0].split('-')[-3]))
                                all_values.append(int(high_temp[0]))
                                all_values.append(int(low_temp[0]))
                                all_values.append(int(mean_humidity[0]))
                            except ValueError:
                                pass
                        # verifying data in main list.
                        if len(all_values) == 6:
                            max_temp.append(all_values)
    return max_temp


def get_data_chart(directory):

    all_values = []
    month = {
        '1': 'Jan',
        '2': 'Feb',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    for dir, subdir, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                with open(os.path.join(directory, filename), 'r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for line in csv_reader:
                        # one list of temperature and dates
                        temp_dates = []
                        # list of Max Temperature
                        max_temp = line[1:2]
                        # list of Min Temperature
                        min_temp = line[3:4]
                        # list of dates
                        date = line[0:1]
                        if len(max_temp) >= 1 and len(min_temp) >= 1:
                            try:
                                # adding day in list.
                                temp_dates.append(int(date[0].split('-')[-1]))
                                # adding month in list.
                                temp_dates.append(month[str(int(date[0].split('-')[-2]))])
                                # adding year in list.
                                temp_dates.append(int(date[0].split('-')[-3]))
                                # adding temperature in list.
                                temp_dates.append(int(max_temp[0]))
                                temp_dates.append(int(min_temp[0]))
                            except ValueError:
                                pass
                            # verifying data in list.
                            if len(temp_dates) == 5:
                                all_values.append(temp_dates)
    return all_values

