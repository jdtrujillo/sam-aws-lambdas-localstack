import json
import boto3
import os
import logging

# Configurar logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Inicializar recursos fuera del handler para optimizar invocaciones cálidas (warm starts)
endpoint = os.environ.get("DYNAMODB_ENDPOINT")
dynamodb = boto3.resource(
    "dynamodb", endpoint_url=endpoint, region_name="us-east-1"
)
table = dynamodb.Table("Libros")


def lambda_handler(event, context):
    logger.info("Iniciando obtención de libros")
    
    try:
        # Hacemos un scan de toda la tabla
        response = table.scan()
        items = response.get("Items", [])
        
        logger.info(f"Se obtuvieron {len(items)} libros exitosamente")
        return {
            "statusCode": 200, 
            "body": json.dumps(items)
        }
    except Exception as e:
        logger.error(f"Error al obtener libros: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error interno del servidor"})
        }
