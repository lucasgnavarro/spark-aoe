import os

# Variables
MY_TEST_VARIABLE = 'TEST'

# Database
DB_USER = os.getenv('DB_USER', 'wololo')
DB_PASS = os.getenv('DB_PASS', 'wololo')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5445')
DB_NAME = os.getenv('DB_NAME', 'aoe')
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# AOE Endpoints
AOE_CIVILIZATIONS = "https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations"
AOE_UNITS= "https://age-of-empires-2-api.herokuapp.com/api/v1/units"
AOE_STRUCTURES = "https://age-of-empires-2-api.herokuapp.com/api/v1/structures"
AOE_TECHNOLOGIES = "https://age-of-empires-2-api.herokuapp.com/api/v1/technologies"


