# README 

Simple api for infromation about airports in different country.


## Installation
Use git:
```
git clone https://github.com/seregagavrilov/airports
pip install -r requirements.txt
```
## How to use                  
You should to load data for csv file into data base.                 
```
python manage.py load_airports /Users/sergeigavrilov/airports_directory/task-1_apinfo.ru.csv
```
## Run aplication
For run application you can use localhost or deploy this on any server. 
How deploy you can read from oficial documintation https://docs.djangoproject.com/en/2.1/howto/deployment/
```
 python ./manage.py runserver```
```
And that's all! Enjoy!
