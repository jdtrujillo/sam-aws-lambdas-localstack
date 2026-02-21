import json
import boto3
import os
import logging

# Configurar logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Inicializar recursos fuera del handler para optimizar invocaciones cálidas (warm starts)
# Obtenemos la URL de LocalStack desde las variables de entorno
endpoint = os.environ.get("DYNAMODB_ENDPOINT")
# Configuramos boto3 para que apunte a LocalStack
dynamodb = boto3.resource(
    "dynamodb", endpoint_url=endpoint, region_name="us-east-1"
)
table = dynamodb.Table("Libros")


def lambda_handler(event, context):
    logger.info("Iniciando guardado de libro")
    
    try:
        # Extraemos los datos del evento (simulando una petición HTTP)
        body_str = event.get("body", "{}")
        body = json.loads(body_str) if isinstance(body_str, str) else body_str
        
        item_id = body.get("id")
        nombre = body.get("nombre")
        autor = body.get("autor")
        
        if not item_id or not nombre or not autor:
            logger.warning("Faltan campos requeridos (id, nombre, autor)")
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Faltan campos requeridos"})
            }

        logger.info(f"Guardando libro con id: {item_id}, nombre: {nombre}")
        
        # Guardamos en DynamoDB
        table.put_item(Item={"id": item_id, "nombre": nombre, "autor": autor})

        logger.info("Libro guardado exitosamente")
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Libro guardado exitosamente", "libro": {"id": item_id, "nombre": nombre, "autor": autor}}),
        }
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON del body: {str(e)}")
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "El cuerpo de la petición no es un JSON válido"})
        }
    except Exception as e:
        logger.error(f"Error al guardar libro: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error interno del servidor"})
        }
