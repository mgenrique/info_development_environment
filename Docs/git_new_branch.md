
# Estrategia de Ramas: Estado Congelado y Desarrollo en `dev`

Este archivo describe cómo mantener una rama con el estado actual del proyecto "congelado" y continuar el desarrollo en una rama `dev`. Sigue estos pasos para configurar correctamente tu flujo de trabajo en GitHub.

## 1. Crea una nueva rama para "congelar" el estado actual

Primero, debes crear una nueva rama basada en el estado actual del repositorio. Vamos a llamarla `release0`, que contendrá el estado congelado del proyecto.

```bash
git checkout -b release0
```

Esto crea una nueva rama `release0` basada en el estado actual del repositorio.

## 2. Sube la nueva rama a GitHub

Para almacenar esta nueva rama en GitHub, súbela con el siguiente comando:

```bash
git push origin release0
```

Esto subirá la rama `release0` a tu repositorio remoto, donde se conservará el estado "congelado". No deberás hacer más cambios en esta rama a partir de ahora.

## 3. Crea o cambia a la rama de desarrollo (`dev`)

Ahora que tienes la rama `release0` para el estado congelado, puedes crear y empezar a trabajar en la rama de desarrollo `dev`. Si no tienes esta rama, créala con:

```bash
git checkout -b dev
```

Si ya tienes la rama `dev`, simplemente cambia a ella:

```bash
git checkout dev
```

## 4. Trabaja en la rama `dev`

A partir de este punto, deberás realizar todos tus commits y desarrollo en la rama `dev`. Así podrás continuar con las mejoras, correcciones o nuevas características sin alterar la rama `release0`. 

## 5. Sube la rama `dev` a GitHub

Cuando hayas terminado de trabajar en la rama `dev`, sube los cambios a GitHub si aún no lo has hecho:

```bash
git push origin dev
```

## 6. Protege la rama `release0` (opcional)

Si deseas asegurarte de que la rama `release0` no se modifique accidentalmente, puedes protegerla en GitHub. Para hacer esto:

1. Ve al repositorio en GitHub.
2. Dirígete a la pestaña **Settings**.
3. En el menú lateral, selecciona **Branches**.
4. Crea una nueva regla en **Branch protection rules** para proteger la rama `release0`.
5. Puedes habilitar la opción de "Restrict who can push to this branch" para evitar modificaciones no deseadas.

## Resumen

- Crea la rama `release0` para congelar el estado actual del proyecto.
- Cambia o crea la rama `dev` para seguir desarrollando.
- Protege la rama `release0` si es necesario para evitar modificaciones accidentales.

Este flujo de trabajo te permite mantener un estado congelado y a la vez seguir desarrollando en paralelo.
