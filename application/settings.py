import os

SECRET_KEY = '\xb2d\xd3\xad\xbb\x84\r\xd5\xa8\xd7R\x0b\xbf\xb7\xb8\xf7\xd0SF\xabw\xfd\xa9!'

############
# DATABASE #
############

DATABASE_USER = 'sa'
if not DATABASE_USER:
    DATABASE_USER = os.environ['DATABASE_USER']

DATABASE_PASSWORD = 'password1/'
if not DATABASE_PASSWORD:
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']

DATABASE_HOST = 'localhost'
if not DATABASE_HOST:
    DATABASE_HOST = os.environ['DATABASE_HOST']

DATABASE_PORT = '1433'
if not DATABASE_PORT:
    DATABASE_PORT = os.environ['DATABASE_PORT']

DATABASE_NAME = 'photochnaja_db'
if not DATABASE_NAME:
    DATABASE_NAME = os.environ['DATABASE_NAME']

DATABASE_DRIVER = 'ODBC+Driver+17+for+SQL+Server'
if not DATABASE_DRIVER:
    DATABASE_DRIVER = os.environ['DATABASE_DRIVER']

SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(
    DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT,
    DATABASE_NAME, DATABASE_DRIVER)
