# My Custom Controller

Este componente personalizado implementa un controlador PID para ser usado dentro de Home Assistant.

## Archivos importantes

- `manifest.json`: Define las dependencias del componente y las bibliotecas externas necesarias.
- `controller.py`: Contiene la lógica del controlador PID y su integración con Home Assistant.
- `__init__.py`: Archivo inicial que permite cargar el componente en Home Assistant.
- `config_flow.py`: Archivo necesario si se utiliza "config_flow": true y que permite una instalación y configuración grafica del componente

## Archivo __init__.py

El archivo __init__.py es importante para cualquier paquete en Python, incluido un componente personalizado de Home Assistant. 
Este archivo señala que la carpeta my_controller debe ser tratada como un módulo de Python y puede contener la lógica de inicialización del componente.

En el caso de Home Assistant, el archivo __init__.py se utiliza principalmente para:
- Registrar el componente en Home Assistant.
- Inicializar dependencias si es necesario.
- Configurar el comportamiento general del componente.

Contenido mínimo de __init__.py:
En muchos casos, si no hay un proceso de inicialización especial, el archivo puede estar vacío o solo contener las configuraciones básicas del componente.

## Dependencias

Este componente depende de:
- `sensor`: Utilizado para obtener datos de sensores como la temperatura.
- `mqtt`: Para la comunicación con dispositivos a través de MQTT.

## Requisitos

Las siguientes bibliotecas externas de Python son necesarias:
- `numpy>=1.19.0`
- `scipy>=1.5.0`

## Configuración
Al haber usado en manifest.json la entrada "config_flow": true y haber creado el archivo config_flow.py no será necesaria incluir la siguiente entrada al archivo `configuration.yaml` para habilitar el componente:

```yaml
sensor:
  - platform: my_controller
    kp: 1.0
    ki: 0.1
    kd: 0.01
    setpoint: 25  
```
De esta forma es posible hacer funcionar el componente con los siguientes pasos:
- Abre la GUI de Home Assistant.
- Navega a Settings > Devices & Services.
- Haz clic en Add Integration.
- Busca o selecciona el componente "My Controller"

