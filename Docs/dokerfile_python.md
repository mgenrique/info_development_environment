# Ejemplo de Dockerfile para una aplicación Python (Flask)
Ejemplo de un **Dockerfile** para una aplicación Python sencilla, que utiliza `Flask` como marco web:
```dockerfile
# Usar una imagen base de Python 3.9
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al directorio de trabajo en el contenedor
COPY . .

# Exponer el puerto en el que la aplicación va a ejecutarse
EXPOSE 5000

# Definir el comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]
```

### Explicación de cada parte del Dockerfile:

1. **FROM python:3.9-slim**: Se usa una imagen ligera de Python 3.9 como base. Esta imagen contiene Python y un sistema operativo mínimo basado en Debian.
   
2. **WORKDIR /app**: Establece el directorio de trabajo dentro del contenedor donde se copiarán los archivos de la aplicación.

3. **COPY requirements.txt .**: Copia el archivo `requirements.txt` desde el directorio actual al directorio de trabajo del contenedor.

4. **RUN pip install --no-cache-dir -r requirements.txt**: Instala las dependencias de Python listadas en `requirements.txt`. La opción `--no-cache-dir` evita que `pip` almacene archivos de caché, haciendo que el contenedor sea más ligero.

5. **COPY . .**: Copia todo el contenido del directorio de la aplicación al contenedor.

6. **EXPOSE 5000**: Expone el puerto 5000, que es el puerto predeterminado donde Flask ejecuta su servidor web.

7. **CMD ["python", "app.py"]**: Define el comando por defecto que se ejecuta al iniciar el contenedor. En este caso, ejecuta la aplicación Python (`app.py`).

### Archivo `requirements.txt` de ejemplo

Este archivo contiene las dependencias necesarias para la aplicación:

```
Flask==2.0.3
```

### Estructura del proyecto

La estructura del proyecto podría verse así:

```
/mi-app
  ├── Dockerfile
  ├── requirements.txt
  └── app.py
```

### Archivo `app.py` de ejemplo

Este archivo es el código de la aplicación Flask:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo desde Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Construir y ejecutar el contenedor

1. **Construir la imagen**:

   ```bash
   docker build -t flask-app .
   ```

2. **Ejecutar el contenedor**:

   ```bash
   docker run -p 5000:5000 flask-app
   ```

Esto ejecutará la aplicación Flask en el puerto 5000 y será accesible en `http://localhost:5000`.

Este es un ejemplo básico que puedes adaptar según las necesidades de tu aplicación Python.
