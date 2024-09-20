# Covertir código en lenguaje `PlantUML` a Python con la libreria `statemachine`

Una vez que tenemos definida una máquina de estados en lenguaje `PlantUML` tal como se ha explicado en [sm_plantuml](sm_plantuml.md), podemos plantear su implementación en Python utilizando la librería `statemachine`

A continuación se muestra un ejemplo de como usar la librería `statemachine` de Python.

Primero, asegúrate de instalar la librería `statemachine` si no la tienes instalada:

```bash
pip install python-statemachine
```

Luego, el siguiente código en Python implementa tu máquina de estados:

```python
from statemachine import State, StateMachine

# Definimos los estados
class CicloStateMachine(StateMachine):
    E1 = State("ESPERAR NUEVO CICLO", initial=True)
    E2 = State("ESPERAR SENSORES")
    E3 = State("VERIFICAR INVERSOR")
    E4 = State("CALCULAR SALIDAS")
    E5 = State("ACTUALIZAR SALIDAS")

    # Transiciones
    fork_state_1 = E1.to(E2) | E1.to(E3)  # El fork va de E1 a E2 y E3
    join_state_1 = E2.to(E4) & E3.to(E4)  # Join combina E2 y E3 en E4
    calcular_a_actualizar = E4.to(E5)
    finalizar = E5.to(E1)  # Retorno al estado inicial para nuevo ciclo

    def on_fork_state_1(self):
        print("Fork: Esperar sensores e inversor")

    def on_join_state_1(self):
        print("Join: Ambos sensores e inversor están OK, calcular salidas")

    def on_E2(self):
        print("Esperando sensores...")

    def on_E3(self):
        print("Verificando inversor...")

    def on_E4(self):
        print("Calculando salidas...")

    def on_E5(self):
        print("Actualizando salidas...")

# Máquina de estados
ciclo = CicloStateMachine()

# Simulación de eventos
def ejecutar_maquina_de_estados(t, t_last, Tm, sensors_ok, inverter_ok, calcs_ok):
    if t - t_last > Tm:
        ciclo.fork_state_1()  # Transición del estado E1 al fork E2 y E3

        if sensors_ok:
            ciclo.E2()
        if inverter_ok:
            ciclo.E3()

        if sensors_ok and inverter_ok:
            ciclo.join_state_1()  # Join para avanzar al estado E4

        if calcs_ok:
            ciclo.calcular_a_actualizar()  # Transición al estado E5

        ciclo.finalizar()  # Volver a E1 para nuevo ciclo

# Ejemplo de uso
t = 100
t_last = 50
Tm = 30
sensors_ok = True
inverter_ok = True
calcs_ok = True

# Ejecutar la máquina de estados
ejecutar_maquina_de_estados(t, t_last, Tm, sensors_ok, inverter_ok, calcs_ok)
```

### Explicación:

1. **Estados**: Se definen los estados `E1` a `E5`, que representan las fases de la máquina de estados.
2. **Transiciones**:
   - `fork_state_1`: Esta transición representa el paso desde `E1` hacia los estados `E2` y `E3` simultáneamente (un fork).
   - `join_state_1`: Une las transiciones de `E2` y `E3` para avanzar a `E4`.
   - `calcular_a_actualizar`: Va de `E4` a `E5` si los cálculos están bien.
   - `finalizar`: Desde `E5` regresa a `E1` para reiniciar el ciclo.
3. **Simulación de eventos**: La función `ejecutar_maquina_de_estados` simula el paso del tiempo y verifica las condiciones para activar las transiciones entre estados.

### Comportamiento:
- La máquina empieza en `E1` y verifica si debe iniciar un nuevo ciclo basándose en el tiempo.
- Luego, pasa a esperar por los sensores (`E2`) y verificar el inversor (`E3`).
- Si ambos están listos (`sensors_ok` y `inverter_ok`), la máquina pasa a calcular las salidas (`E4`), y finalmente, a actualizar las salidas (`E5`).

Este código es un buen punto de partida. ¿Te gustaría agregar o modificar algo?
