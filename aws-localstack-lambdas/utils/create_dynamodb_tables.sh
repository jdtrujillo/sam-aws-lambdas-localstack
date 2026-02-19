#!/bin/bash

# Se usa awslocal para crear la tabla DynamoDB en LocalStack. Para usar en AWS real, reemplaza 'awslocal' por 'aws' y asegúrate de configurar tus credenciales de AWS correctamente.
awslocal dynamodb create-table \
    --table-name Libros \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --profile localstack
