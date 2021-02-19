from os import getenv, pardir
from os.path import dirname, join, realpath

#from dotenv import load_dotenv

PROJECT_ROOT = join(dirname(realpath(__file__)), pardir)

STAGE = getenv('STAGE')
MY_TEST_VARIABLE = 'TEST'
DB_USER = getenv('DB_USER', 'wololo')
DB_PASS = getenv('DB_PASS', 'wololo')
DB_HOST = getenv('DB_HOST', 'localhost')
DB_PORT = getenv('DB_PORT', '5432')
DB_NAME = getenv('DB_NAME', 'aoe')
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# External apis
API_DOG_CEO_URL = 'https://dog.ceo/api'
