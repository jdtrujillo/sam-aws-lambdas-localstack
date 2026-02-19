import json
import boto3
import os


def lambda_handler(event, context):
    # Obtenemos la URL de LocalStack desde las variables de entorno
    endpoint = os.environ.get("DYNAMODB_ENDPOINT")

    # Configuramos boto3 para que apunte a LocalStack
    dynamodb = boto3.resource(
        "dynamodb", endpoint_url=endpoint, region_name="us-east-1"
    )
    table = dynamodb.Table("Libros")

    # Extraemos los datos del evento (simulando una petición HTTP)
    body = json.loads(event.get("body", "{}"))
    item_id = body.get("id")
    nombre = body.get("nombre")
    autor = body.get("autor")

    # Guardamos en DynamoDB
    table.put_item(Item={"id": item_id, "nombre": nombre, "autor": autor})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Libro guardado exitosamente", "libro": body}),
    }
