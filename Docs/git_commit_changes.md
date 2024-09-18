
# Reflejar Cambios Locales en un Fork

Este archivo describe cómo puedes reflejar los cambios locales que has realizado en un *fork* de otro repositorio. A continuación te explico el flujo para asegurarte de que tu *fork* esté actualizado con tus cambios locales y luego subirlos a GitHub.

## Pasos para Reflejar Cambios Locales en tu Fork

### 1. Verifica los cambios locales
Primero, asegúrate de que tienes los cambios locales que deseas reflejar en tu *fork*. Usa este comando para verificar el estado de tu repositorio:

```bash
git status
```

Si ves cambios no *commiteados*, asegúrate de hacer *commit* de ellos.

### 2. Realiza un *commit* de los cambios locales
Si tienes cambios sin guardar, realiza un *commit* para registrarlos:

```bash
git add .
git commit -m "Descripción de los cambios realizados"
```

Esto añadirá tus cambios locales al historial del repositorio.

### 3. Configura el remoto si es necesario
Si no lo has hecho antes, asegúrate de que tu repositorio *fork* está configurado correctamente como remoto. Para verificar qué remotos tienes configurados, usa:

```bash
git remote -v
```

Deberías ver algo similar a:

```
origin  https://github.com/mgenrique/NOMBRE_DEL_FORK.git (fetch)
origin  https://github.com/mgenrique/NOMBRE_DEL_FORK.git (push)
```

Si no lo tienes, puedes configurarlo así:

```bash
git remote add origin https://github.com/mgenrique/NOMBRE_DEL_FORK.git
```

### 4. Sube los cambios al *fork* en GitHub
Ahora que tienes los cambios locales *commiteados* y el remoto configurado, puedes subirlos a tu *fork* en GitHub usando:

```bash
git push origin <nombre_rama>
```

Por ejemplo, si estás trabajando en la rama `dev`:

```bash
git push origin dev
```

### 5. Actualiza el repositorio original si es necesario (opcional)
Si quieres que los cambios que has hecho en tu *fork* se reflejen en el repositorio original del cual hiciste *fork*, deberás abrir un **Pull Request (PR)**. Para hacerlo:

1. Ve a GitHub y abre tu repositorio *fork*.
2. Haz clic en el botón de **Compare & pull request** que debería aparecer en la parte superior.
3. Llena los detalles del PR y envíalo.

Este PR solicitará que tus cambios se integren en el repositorio original.

## Resumen
1. Verifica y haz *commit* de tus cambios locales.
2. Asegúrate de que el remoto está configurado correctamente.
3. Usa `git push origin <nombre_rama>` para subir los cambios a tu *fork* en GitHub.
4. Si quieres reflejar estos cambios en el repositorio original, abre un **Pull Request** en GitHub.

Este flujo te permitirá reflejar tus cambios locales en el *fork* y, si lo deseas, proponer que se incluyan en el repositorio original.
