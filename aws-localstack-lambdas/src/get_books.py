import json
import boto3
import os


def lambda_handler(event, context):
    endpoint = os.environ.get("DYNAMODB_ENDPOINT")
    dynamodb = boto3.resource(
        "dynamodb", endpoint_url=endpoint, region_name="us-east-1"
    )
    table = dynamodb.Table("Libros")

    # Hacemos un scan de toda la tabla
    response = table.scan()
    items = response.get("Items", [])

    return {"statusCode": 200, "body": json.dumps(items)}
