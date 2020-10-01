import os
from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_User = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
