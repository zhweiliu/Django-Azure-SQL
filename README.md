# Django-Azure-SQL

It's a sample to connect to Azure database using by Django, and I only try it successful on Mac


## Step 1 : Install unixODBC

Follow the tips by article : [Install FreeTDS, unixODBC and pyodbc on OS X](https://gist.github.com/Bouke/10454272)


First install the following libraries :
```
$ brew install unixodbc
$ brew install freetds --with-unixodbc
```
---


## Step 2 : Install Python libraries
Follow the tips by article :  [django-pyodbc-azure](https://github.com/michiya/django-pyodbc-azure)

The second, continue onto installing the Python libraries pyodbc and Django:
```
$ python -m pip install pyodbc
$ python -m pip install django
```

and then, start up your django server and check it works.
![Alt text](https://i.imgur.com/66KAWNF.png)
---

## Setp 3 : Setup django-pyodbc-azure

Change datebase setting of {PROJECT_NAME}/settings.py in project folder

For example, this project will be deploy on Heroku, so I used environment variable to set the parameters of DATABASE
```
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': {SQL_DATABASES_NAME},
        'USER': {SQL_DATABASES_USER},
        'PASSWORD': {SQL_DATABASES_PASSWORD},
        'HOST': {SQL_DATABASES_HOST},
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    }
}
```



to get the environment variables via

`os.environ.get({PARAM_NAME}, DEFAULT_RETURN)`

such as :
```
DATABASES_NAME = os.environ.get('DATABASES_NAME', None)
DATABASES_USER = os.environ.get('DATABASES_USER', None)
DATABASES_PASSWORD = os.environ.get('DATABASES_PASSWORD', None)
DATABASES_HOST = os.environ.get('DATABASES_HOST', None)
```

> #### Notices :
> 	If any error message when DATABASE set done, such as
>
>> "[unixODBC][Microsoft][ODBC Driver 13 for SQL Server]"
>>
>  check
>> 1. Is unixodbc library install successful ?
>> 2. Is any firewall rules on your database , and you haven't follow it?
---

## Final : Integrating tables to Django

Follow the tips by article : [Integrating Django with a legacy database](https://docs.djangoproject.com/en/1.11/howto/legacy-databases/)

> ###### Or you can follow tips of here two article, if you can read chinese
>> 1. [Django inspectdb ????Table????models.py](https://dotblogs.com.tw/andrewblog/2017/09/19/104547)
>>
>> 2. [???????????](http://djangobook.py3k.cn/2.0/chapter18/)


Django comes with a utility called inspectdb that can create models by introspecting an existing database, and save this as a file by using standard Unix output redirection:

(Before this, you should check Django has success connected to SQL database)

```
$ python manage.py inspectdb > models.py
```

and modify the managed field of class Meta of model which you need django to help you manage each table's creation, modification, and deletion, such as :
```
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=70)
    class Meta:
       # managed = False # Django not to manage this model
       managed = True # Django will to manage this model
       db_table = 'CENSUS_PERSONS'
```
---

## Experience of me
> It is difficult to integrat Django and Azure sql database, because I want via Django-admin,a graphics user interface, to manage user .
>
> But it's occur filed name collision caused by keyword, so I tried migrate twice , and upgrade source code about database cursor to fix this problem
>
> I suggest you do not try this solution if Django-admin was not necessary for manage SQL database.
---
> ##### What the mind of man can conceive and believe, it can achieve.
> ##### Author : ZhengWei, Liu
> ##### contact : zhweiliu@gmail.com
