# README 


## Installation
Use git:
```
git clone https://github.com/seregagavrilov/airports
pip install -r requirements.txt
```
## How to use                  
You should load data for csv file into data base.                 
```
python manage.py load_airports /Users/sergeigavrilov/airports_directory/task-1_apinfo.ru.csv
```
## Run application
For run application you can use localhost or deploy this on any server. 
How deploy you can read from oficial documintation https://docs.djangoproject.com/en/2.1/howto/deployment/.
For run on localhost you can write simple command:
```
 python ./manage.py runserver
```
## Use appplication
For information about airports:

```
http://localhost:8000/airports_api/v1/airports/
```

You can use filter:
```
http://localhost:8000/airports_api/v1/airports/?city__country__eng_name=Pakistan
```
And that's all! Enjoy!
