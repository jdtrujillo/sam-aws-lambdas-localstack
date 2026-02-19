import json


def lambda_handler(event, context):
    # Extraemos el nombre del evento. Si no viene, usamos "Desconocido" por defecto.
    nombre = event.get("nombre", "Desconocido")
    mensaje = f"¡Hola, {nombre}! Este es un saludo desde tu Lambda local."

    return {"statusCode": 200, "body": json.dumps({"mensaje": mensaje})}
