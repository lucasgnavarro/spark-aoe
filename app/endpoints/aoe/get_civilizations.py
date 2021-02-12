import requests
import json
from app.settings import AOE_CIVILIZATIONS

def lambda_handler(event, context):
    """ Get the Civilizations data from AOE """
    
    r = requests.get(AOE_CIVILIZATIONS)
    body = {"civilizations": []}

    if (r.status_code == requests.codes.ok):
        body = r.text

    return {"statusCode": 200, "body": json.dumps(body)}