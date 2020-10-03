import os
from urllib import parse
from decouple import config


def _build_db_connection_string() -> str:
    db_user = config('db_user')
    db_password = config('db_password')
    db_server = config('db_server')
    db_name = config('db_name')
    params = parse.quote_plus(
        r'Driver={ODBC Driver 17 for SQL Server};Server=' + db_server +
        ';Database=' + db_name +
        ';Uid=' + db_user +
        ';Pwd=' + db_password +
        ';Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=5;')

    connection_string = f'mssql+pyodbc:///?odbc_connect={params}'
    return connection_string


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = _build_db_connection_string()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
