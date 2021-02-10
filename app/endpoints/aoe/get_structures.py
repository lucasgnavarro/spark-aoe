import requests
import json
from app.settings import AOE_STRUCTURES

def lambda_handler(event, context):
    """ Get the Structures data from AOE """
    
    r = requests.get(AOE_STRUCTURES)
    body = {"structures": []}

    if (r.status_code == requests.codes.ok):
        body = r.text

    return {"statusCode": 200, "body": json.dumps(body)}
