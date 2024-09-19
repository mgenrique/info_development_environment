LINTERS
Un **linter** es una herramienta que analiza el código fuente para detectar errores, problemas de estilo y posibles bugs antes de ejecutar el código. Proporciona sugerencias para mejorar la calidad del código y garantizar que cumpla con las normas de codificación establecidas.

- **Errores**: Detecta errores sintácticos y semánticos.
- **Estilo**: Verifica que el código siga las convenciones de estilo y formato.
- **Calidad**: Identifica patrones de código que podrían ser problemáticos o que no cumplen con las mejores prácticas.

Usar un linter ayuda a mantener el código limpio, legible y libre de errores comunes.

En Python, los linters más habituales son:

1. **Pylint**: Es uno de los linters más completos y configurables para Python. Ofrece un análisis exhaustivo del código, verificando errores, convenciones de estilo, y calidad del código.

2. **Flake8**: Combina las funcionalidades de `PyFlakes` (para detectar errores) y `pycodestyle` (para verificar el estilo de código). Es conocido por ser rápido y tener configuraciones menos estrictas que `Pylint`.

3. **Black**: Aunque técnicamente es un formateador en lugar de un linter, `Black` se utiliza para aplicar un formato uniforme al código Python, siguiendo convenciones de estilo predefinidas.

4. **Pyflakes**: Se centra en encontrar errores en el código y es más ligero que `Pylint` y `Flake8`. Es útil para detección rápida de errores.

Cada uno tiene sus ventajas, y la elección suele depender de las necesidades específicas del proyecto o las preferencias del equipo.
