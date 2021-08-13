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

def main(path):
    rain_data = read_file(path)
    headers, clean_data = clean_and_select_data(rain_data)
    list_of_data_dicts = create_dict(headers, clean_data)
    for data_dict in list_of_data_dicts[0:10]:
        print(data_dict)

main(path)
