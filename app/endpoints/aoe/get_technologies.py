import requests
import json
from app.settings import AOE_TECHNOLOGIES

def lambda_handler(event, context):
    """ Get the Techonologies data from AOE """
    
    r = requests.get(AOE_TECHNOLOGIES)
    body = {"technologies": []}

    if (r.status_code == requests.codes.ok):
        body = r.text

    return {"statusCode": 200, "body": json.dumps(body)}