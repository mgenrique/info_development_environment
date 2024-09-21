Para subir la carpeta local `/home/enrique/ha_vsc_01` a la carpeta `VSC_files` en tu repositorio GitHub `https://github.com/mgenrique/dev_ha_cc_pv_controller/tree/main/VSC_files`, puedes seguir estos pasos:

### 1. **Accede a la carpeta local del repositorio**
Primero, abre una terminal y navega a la carpeta donde has clonado tu repositorio `dev_ha_cc_pv_controller`. Si aún no lo has clonado, clónalo con el siguiente comando:

```bash
git clone https://github.com/mgenrique/dev_ha_cc_pv_controller.git
```

Navega al directorio del repositorio clonado:

```bash
cd dev_ha_cc_pv_controller
```

### 2. **Copia los archivos locales a la carpeta `VSC_files`**

Si no existe la carpeta `VSC_files`, créala dentro del repositorio. Si ya existe, puedes proceder directamente a copiar los archivos:

```bash
mkdir -p VSC_files
cp -r /home/enrique/ha_vsc_01/* VSC_files/
```

Esto copiará el contenido de la carpeta `/home/enrique/ha_vsc_01` dentro de la carpeta `VSC_files` de tu repositorio.

### 3. **Añadir los cambios al control de versiones**

Ahora, agrega los cambios al control de versiones de Git:

```bash
git add VSC_files/*
```

### 4. **Realiza un commit de los cambios**

Una vez agregados los archivos, realiza un *commit* con un mensaje descriptivo:

```bash
git commit -m "Añadir archivos de ha_vsc_01 a la carpeta VSC_files"
```

### 5. **Subir los cambios al repositorio en GitHub**

Finalmente, sube los cambios al repositorio remoto (`main` o la rama en la que estés trabajando):

```bash
git push origin main
```

### Resumen:
1. Navega al directorio del repositorio.
2. Copia los archivos locales a la carpeta `VSC_files`.
3. Añade los cambios con `git add`.
4. Realiza un *commit*.
5. Sube los cambios al repositorio remoto con `git push`.

Después de realizar estos pasos, los archivos de la carpeta `/home/enrique/ha_vsc_01` se encontrarán en la carpeta `VSC_files` de tu repositorio en GitHub.
