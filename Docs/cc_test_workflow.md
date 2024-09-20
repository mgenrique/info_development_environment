# Flujo de trabajo para probar y depurar componentes personalizados de Home Assistant

Para probar y depurar tu componente personalizado en Home Assistant, te recomiendo un flujo de trabajo estructurado que te permita identificar y corregir errores de manera eficiente. Aquí tienes una guía paso a paso para llevar a cabo este proceso:

#### 1. **Prepara tu entorno de desarrollo**:
   - **Instala Home Assistant en un entorno de desarrollo**:
     - Puedes usar **Home Assistant Core** instalado en tu máquina o en un entorno Docker.
     - Alternativamente, si prefieres trabajar con contenedores, puedes usar **Dev Containers** con Visual Studio Code (lo que ya has mencionado que has probado anteriormente).
   
   - **Configura tu entorno virtual (opcional)**:
     - Si trabajas con Home Assistant Core directamente, es recomendable usar un entorno virtual para aislar las dependencias:
       ```bash
       python3 -m venv venv
       source venv/bin/activate
       pip install homeassistant
       ```

#### 2. **Coloca el componente en la carpeta correcta**:
   - Coloca tu componente en la carpeta `custom_components` dentro de tu directorio de configuración de Home Assistant.
   - La estructura debe verse así:
     ```
     /config
       └── custom_components
           └── pv_controller
               ├── __init__.py
               ├── manifest.json
               ├── sensor.py
               ├── config_flow.py
               ├── state_machine.py
               ├── const.py
     ```

#### 3. **Activa el logging detallado para tu componente**:
   - Configura el logging de Home Assistant para que te proporcione detalles importantes durante la ejecución de tu componente. Esto es clave para depurar los errores.
   - Añade lo siguiente en tu archivo `configuration.yaml` para aumentar el nivel de logging:
     ```yaml
     logger:
       default: warning
       logs:
         custom_components.pv_controller: debug
     ```

   - Esto te permitirá ver registros detallados específicos de tu componente personalizado.

#### 4. **Reinicia Home Assistant**:
   - Después de colocar tu componente y configurar el logging, reinicia Home Assistant para que cargue el componente.
     - Si trabajas en **Home Assistant Core**, puedes hacer esto desde la línea de comandos:
       ```bash
       hass --config /ruta/a/tu/config
       ```

   - Si trabajas en una versión de Home Assistant con interfaz web, puedes reiniciarlo desde **Configuración -> Controles del servidor -> Reiniciar**.

#### 5. **Añade el componente en la interfaz**:
   - Ve a la interfaz web de Home Assistant y navega a **Configuración -> Dispositivos y Servicios**.
   - Busca tu componente `PV Controller` y sigue el flujo de configuración que has creado.
   - Asegúrate de que los parámetros que ingreses sean válidos (como la API Key de ESIOS y Forecast Solar, coordenadas geográficas, etc.).

#### 6. **Verifica el registro de Home Assistant**:
   - Después de que el componente se cargue, verifica los **logs** de Home Assistant.
     - Puedes ver los logs en la interfaz web de Home Assistant, en **Herramientas para desarrolladores -> Registro**.
     - También puedes acceder al archivo de registro (`home-assistant.log`) en el directorio de configuración de Home Assistant.
   - Busca mensajes de depuración relacionados con tu componente (`custom_components.pv_controller`).

#### 7. **Prueba los sensores**:
   - Desde la interfaz de Home Assistant, ve a **Herramientas para desarrolladores -> Estados**.
   - Busca los sensores que has definido (`sensor.pvpc_sensor`, `sensor.solar_forecast_sensor`, `sensor.pv_controller_state`) y verifica si se están actualizando correctamente y si sus estados son los esperados.

#### 8. **Depura errores utilizando `raise_for_status()` y excepciones**:
   - Asegúrate de que el manejo de errores en las llamadas a las APIs esté funcionando correctamente. Verifica si `raise_for_status()` lanza excepciones cuando las llamadas fallan, y si los errores aparecen en los logs.
   - Si alguna llamada a la API falla, verifica que los sensores cambien su estado a `"error"` y registra el motivo del fallo en los logs.

#### 9. **Modifica el código y recarga sin reiniciar Home Assistant (opcional)**:
   - Para agilizar el proceso de prueba y no tener que reiniciar Home Assistant cada vez que hagas un cambio en el código, puedes recargar componentes personalizados desde la interfaz:
     - **Configuración -> Controles del servidor -> Recargar componentes personalizados**.
   - Esto te permite actualizar el código del componente sin tener que reiniciar todo Home Assistant, lo que acelera la depuración.

#### 10. **Verifica la funcionalidad de la máquina de estados**:
   - Asegúrate de que la máquina de estados (`CicloStateMachine`) esté funcionando como se espera.
   - Verifica en el sensor `PVControllerStateSensor` que el estado de la máquina de estados refleje el estado correcto.
   - Si ves comportamientos inesperados, ajusta los `print` o los logs en los métodos de transición de la máquina de estados.

#### 11. **Prueba la frecuencia de actualización (`Throttle`)**:
   - Verifica que la frecuencia de actualización de los sensores (como la llamada a Forecast Solar) respete el tiempo mínimo definido por `MIN_TIME_BETWEEN_UPDATES_SOLARFORECAST`.
   - Comprueba en los logs si el decorador `@Throttle` está funcionando correctamente y limitando las llamadas API.

#### 12. **Haz ajustes según los resultados de las pruebas**:
   - Si encuentras errores o comportamientos inesperados, usa los logs para identificar el problema.
   - Ajusta el código de tu componente según sea necesario y vuelve a probar hasta que los sensores y la máquina de estados funcionen como se espera.

#### 13. **Itera rápidamente y documenta los cambios**:
   - A medida que vayas solucionando los problemas, realiza commits regulares en tu repositorio de Git para mantener un registro de los cambios.
   - Documenta cualquier aspecto importante o decisiones que tomes durante el proceso de depuración.

### Herramientas útiles:

- **VS Code con Dev Containers**: Si ya has trabajado con Dev Containers en Visual Studio Code, puedes seguir usándolos para un entorno de desarrollo totalmente aislado.
- **Git**: Realiza commits regularmente para guardar el progreso y revertir cambios si es necesario.
- **Linter y herramientas de calidad de código**: Usa herramientas como `flake8` o `pylint` para asegurarte de que tu código sigue las mejores prácticas de estilo de Python.

### Resumen del flujo de trabajo:

1. Prepara tu entorno y coloca el componente en `custom_components`.
2. Configura el logging detallado en `configuration.yaml`.
3. Reinicia Home Assistant y registra tu componente.
4. Verifica los logs y prueba los sensores en la interfaz.
5. Depura cualquier error encontrado en los logs.
6. Prueba la máquina de estados y la frecuencia de actualización de los sensores.
7. Realiza ajustes, recarga el componente y repite el proceso hasta que todo funcione correctamente.

Con este flujo de trabajo, podrás probar y depurar eficientemente tu componente `PVController` en Home Assistant. ¡Déjame saber si tienes alguna pregunta o si encuentras algún problema en el camino!
