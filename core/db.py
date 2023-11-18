import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE= {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

SQLSERVER={
    'default':{
        'ENGINE': 'mssql',
        'NAME': 'informaticaSimple',
        'USER': 'sa',
        'PASSWORD': 'Brid892240$!',
        'HOST': 'vps2383.baraghost.com',
        'PORT': '9060',
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",
        },
    }
}