import datetime
import re



path = (r"C:\Users\Mark\Desktop\pdx_code\class_lemur\code\mark\portland_rain_data.txt")

def read_file(path):
    with open(path, 'r') as file:
        rain_data = file.read()
        file.close()
    return rain_data

def clean_and_select_data(rain_data):
    split_data = rain_data.split("-->")
    data_table = split_data[1]
    data_table_split = re.split(r'\n', data_table)
    headers = re.findall('[a-zA-Z]+', data_table_split[1])
    data_table_rows = data_table_split[3:]
    for i in range(len(data_table_rows)):
        data_table_rows[i] = re.split('\s+', data_table_rows[i])
    data_table_rows = data_table_rows[:-1]
    for i in range(len(data_table_rows)):
        data_table_rows[i][0] = datetime.datetime.strptime(data_table_rows[i][0], '%d-%b-%Y')
        try:
            data_table_rows[i][1] = int(data_table_rows[i][1])
        except:
            data_table_rows[i][1] = 9999999
    clean_data = [row for row in data_table_rows if not (row[1] == 9999999)]
    return headers, clean_data

def create_dict(headers, data_table):
    
    return_list = []
    for row in data_table:
        new_dict = {}
        for j in range(len(headers)):
            new_dict[headers[j]] = row[j]
        return_list.append(new_dict)
    return return_list

def calculate_mean(rainfall_amounts):
    return (sum(rainfall_amounts)/len(rainfall_amounts))

def calculate_variance(mean, rainfall_amounts):
    return sum((amount-mean)**2 for amount in rainfall_amounts) / len(rainfall_amounts)
    
def find_max_rain(rainfall_amounts, list_of_rainfall_amounts):
    max_rain = max(rainfall_amounts)
    max_dates = [row['Date'] for row in list_of_rainfall_amounts if row['Total'] == max_rain]
    return max_dates, max_rain

def find_max_rain_year(list_of_rainfall_dicts):
    temp_list = []
    for row in list_of_rainfall_dicts:
        year = row['Date'].year
        rainfall = row['Total']
        temp_list.append([year, rainfall])
    years_list = [year[0] for year in temp_list]
    years_set = set(years_list)
    years_count_dict = {}
    for year in years_set:
        years_count_dict[year] = years_list.count(year)
    years_total_dict = {}
    for year in years_set:
        years_total_dict[year] = 0
    for row in temp_list:
        years_total_dict[row[0]] += row[1]
    average_year_dict = {}
    for year in years_set:
        average_year_dict[year] = round(years_total_dict[year]/years_count_dict[year],2)
    max_average_year_value = max(average_year_dict.values())
    for key,value in average_year_dict.items():
        if max_average_year_value == value:
            max_average_year = key
    return max_average_year, max_average_year_value 

        


def main(path):
    rain_data = read_file(path)
    headers, clean_data = clean_and_select_data(rain_data)
    list_of_data_dicts = create_dict(headers, clean_data)
    # for data_dict in list_of_data_dicts[0:10]:
    #     print(data_dict)
    rainfall_amounts = [dicts.get("Total") for dicts in list_of_data_dicts]
    mean = calculate_mean(rainfall_amounts)
    print(f"\nThe Mean rainfall amount for this location is {mean}")
    variance = calculate_variance(mean, rainfall_amounts)
    print(f"\nThe Variance of the rainfall for this location is {variance}")
    max_rain_dates, max_rain = find_max_rain(rainfall_amounts, list_of_data_dicts)
    print(f"\nThe date with the highest rainfall is {max_rain_dates[0].strftime('%d-%b-%Y')} with a rainfall of {max_rain}")
    max_average_year, max_average_year_value = find_max_rain_year(list_of_data_dicts)
    print(f"\nThe year with the highest average rainfall is {max_average_year} with an average rainfall of {max_average_year_value}")


main(path)
