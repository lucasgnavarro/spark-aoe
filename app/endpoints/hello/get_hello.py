import json


def lambda_handler(event, context):
    body = {
        "message": "THIS IS A HELLO WORLD",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
