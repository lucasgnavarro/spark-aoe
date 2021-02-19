import json
from app.settings import MY_TEST_VARIABLE

def lambda_handler(event, context):
    body = {
        "message": f"THIS IS A HELLO WORLD {MY_TEST_VARIABLE}",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
