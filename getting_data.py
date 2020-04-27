import csv
import os


class Data:

    def __init__(self):
        self.directory = 'C:/Users/shiek/PycharmProjects/Assignment1/weatherdata/'

    def get_data_temp(self):

        temperatures = []

        for dir, subdir, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                if filename.split('.')[-1] == 'txt':
                    with open(os.path.join(self.directory, filename), 'r') as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        for line in csv_reader:
                            # one list of temperature and dates
                            temp_dates = []
                            # list of Highest temperature
                            h_temp = line[1:2]
                            # list of Lowest temperature
                            l_temp = line[3:4]
                            # list of most humid
                            h_humid = line[7:8]
                            # list of dates
                            date = line[0:1]
                            if len(h_temp) >= 1 and len(l_temp) >= 1 and len(h_humid) >= 1:
                                try:
                                    # adding day in list.
                                    temp_dates.append(int(date[0].split('-')[-1]))
                                    # adding month in list.
                                    temp_dates.append(int(date[0].split('-')[-2]))
                                    # adding year in list.
                                    temp_dates.append(int(date[0].split('-')[-3]))
                                    # adding Highest temperature in list.
                                    temp_dates.append(int(h_temp[0]))
                                    # adding Lowest temperature in list.
                                    temp_dates.append(int(l_temp[0]))
                                    # adding Max Humidity in list.
                                    temp_dates.append(int(h_humid[0]))
                                except ValueError:
                                    pass
                            # verifying data in main list.
                            if len(temp_dates) == 6:
                                temperatures.append(temp_dates)
        return temperatures

    def data_average(self):
        avr_temp = []
        for dir, subdir, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                if filename.split('.')[-1] == 'txt':
                    with open(os.path.join(self.directory, filename), 'r') as csv_file:
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
                                    all_values.append(int(date[0].split('-')[-2]))
                                    # adding year in list.
                                    all_values.append(int(date[0].split('-')[-3]))
                                    all_values.append(int(high_temp[0]))
                                    all_values.append(int(low_temp[0]))
                                    all_values.append(int(mean_humidity[0]))
                                except ValueError:
                                    pass
                            # verifying data in main list.
                            if len(all_values) == 6:
                                avr_temp.append(all_values)
        return avr_temp

    def data_chart(self):

        all_values = []
        for dir, subdir, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                if filename.split('.')[-1] == 'txt':
                    with open(os.path.join(self.directory, filename), 'r') as csv_file:
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
                                    temp_dates.append(int(date[0].split('-')[-2]))
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


data = Data()
