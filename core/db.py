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
        'NAME': 'nombre de la base de datos',
        'USER': 'usuario de la base de datos',
        'PASSWORD': 'password de la base de datos',
        'HOST': 'url al servidor de base de datos',
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",
        },
    }
}