from django.apps import apps
import csv
import pandas as pd

def load_csv():
    # Airport = apps.get_model('rest_api_airports', 'Airport')
    # City = apps.get_model('rest_api_airports', 'City')
    # Airport = apps.get_model('rest_api_airports', 'Country')
    file = '/Users/sergeigavrilov/airports_directory/task-1_apinfo.ru.csv'
    with open(file, newline='', encoding='cp1251') as csv_file:
        reader = csv.reader(csv_file, delimiter='|')
        next(reader)
        for row in reader:
            print(row)

def load_csv_pandas(fname):
    data = pd.read_csv(fname, sep='|', encoding='cp1251')
    atributes = {}
    for row in data.iterrows():
            dedublicatined = row[1].drop_duplicates()
            print(dedublicatined)


if __name__ == '__main__':
    # load_csv()
    load_csv_pandas('/Users/sergeigavrilov/airports_directory/task-1_apinfo.ru.csv')



