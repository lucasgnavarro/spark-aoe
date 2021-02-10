import requests
import json
from app.settings import AOE_UNITS

def lambda_handler(event, context):
    """ Get the Units data from AOE """
    
    r = requests.get(AOE_UNITS)
    body = {"units": []}

    if (r.status_code == requests.codes.ok):
        body = r.text

    return {"statusCode": 200, "body": json.dumps(body)}

