#### Instalar

##### macOS

Usando [Homebrew](https://brew.sh/), ejecuta los siguientes comandos:

```bash
# 1. Docker
brew install docker

# 2. Python 3.12
brew install python@3.12

# 3. AWS CLI
brew install awscli

# 4. AWS Tap
brew tap aws/tap

# 5. AWS SAM CLI
brew install aws-sam-cli

# 6. AWS CLI Local
brew install awscli-local
```

##### Otros Sistemas Operativos

Para instrucciones de instalación en **Windows** y **Linux**, consulta la documentación oficial:

- **Docker**: https://docs.docker.com/get-docker/
- **Python 3.12**: https://www.python.org/downloads/
- **AWS CLI**: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- **AWS SAM CLI**: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
- **AWS CLI Local**: https://docs.localstack.cloud/user-guide/integrations/aws-cli/

---

## 🚀 Cómo Correr los Ejemplos

A continuación, se detalla cómo ejecutar cada uno de los ejemplos de este repositorio.

### 1. `aws-sam-lambdas`

Este ejemplo contiene una Lambda simple que puedes construir y ejecutar localmente con **AWS SAM**.

#### Pasos

1.  **Navega al directorio del proyecto**:
    ```bash
    cd aws-sam-lambdas
    ```

2.  **Construye la aplicación SAM**:
    ```bash
    sam build
    ```
    Este comando compila tu aplicación y prepara los artefactos para la ejecución.

3.  **Invoca la Lambda localmente**:
    ```bash
    sam local invoke -e events/saludo_1.json
    ```
    - Usamos `sam local invoke` para simular la ejecución de la Lambda en un entorno local.
    - El parámetro `-e` especifica un archivo de evento (`saludo_1.json`) que contiene los datos de entrada para la Lambda.

    Verás una salida que confirma la ejecución y el mensaje de saludo.

### 2. `aws-localstack-lambdas`

Este ejemplo es más completo y demuestra cómo usar Lambdas con **DynamoDB** en un entorno totalmente local gracias a **LocalStack**.

#### Pasos

1.  **Inicia LocalStack**:
    Asegúrate de que Docker esté corriendo y luego navega al directorio del proyecto y levanta los servicios:
    ```bash
    cd aws-localstack-lambdas
    docker-compose up -d
    ```
    Esto iniciará un contenedor de LocalStack con el servicio de DynamoDB activado.

2.  **Crea la tabla en DynamoDB**:
    Una vez que LocalStack esté corriendo, abre otra terminal y ejecuta el siguiente script para crear la tabla `Libros`:
    ```bash
    ./utils/create_dynamodb_tables.sh
    ```
    Este script usa `awslocal` para comunicarse con el contenedor de LocalStack.

3.  **Construye la aplicación SAM**:
    Al igual que en el ejemplo anterior, necesitas construir tu aplicación:
    ```bash
    sam build
    ```

4.  **Invoca las Lambdas**:
    Ahora puedes interactuar con las Lambdas para guardar y consultar libros.

    - **Guardar un libro**:
      ```bash
      sam local invoke GuardarLibroFunction -e events/evento_guardar.json
      ```
      Revisa el archivo `evento_guardar.json` para ver la estructura de datos que se envía.

    - **Consultar todos los libros**:
      ```bash
      sam local invoke ConsultarLibrosFunction
      ```

5.  **Detén LocalStack**:
    Cuando hayas terminado, no olvides detener el contenedor:
    ```bash
    docker-compose down
    ```

