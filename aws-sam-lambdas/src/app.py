import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f"Evento recibido: {json.dumps(event)}")
    
    # Extraemos el nombre del evento. Si no viene, usamos "Desconocido" por defecto.
    nombre = event.get("nombre", "Desconocido")
    mensaje = f"¡Hola, {nombre}! Este es un saludo desde tu Lambda local."
    
    logger.info(f"Mensaje generado: {mensaje}")

    response = {"statusCode": 200, "body": json.dumps({"mensaje": mensaje})}
    
    logger.info(f"Respuesta generada: {json.dumps(response)}")
    return response
