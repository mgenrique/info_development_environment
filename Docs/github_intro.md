# MANUALES SOBRE GIT Y GITHUB

En los siguientes documentos se explica como llevar a cabo algunos de los procesos más habituales relacionados con Git y GitHub

## Sincronizar un Fork con su repositorio original
Seguir este manual [dev_git](./dev_git.md)

## Estrategia de Ramas: Estado Congelado y Desarrollo en `dev`
Seguir este manual [git_new_branch](./git_new_branch.md)

## Reflejar Cambios Locales en un Fork
Seguir este manual [git_commit_changes](./git_commit_changes.md)


Para verificar si tu clave SSH está correctamente registrada y vinculada en GitHub y Ubuntu, puedes seguir estos pasos:

### 1. **Verifica si tienes una clave SSH generada en tu sistema**

Abre una terminal en Ubuntu y verifica si tienes una clave SSH existente:

```bash
ls -al ~/.ssh
```

Esto listará el contenido de la carpeta `~/.ssh`. Busca archivos con nombres como `id_rsa` y `id_rsa.pub`. Si ves estos archivos (o similares), significa que ya tienes una clave SSH generada.

Si no ves archivos SSH, puedes generar una clave SSH con:

```bash
ssh-keygen -t rsa -b 4096 -C "tu_email@ejemplo.com"
```

Esto generará una clave SSH. Cuando se te pregunte dónde guardar el archivo, presiona `Enter` para aceptar la ubicación predeterminada (`~/.ssh/id_rsa`).

### 2. **Verifica que tu clave SSH esté registrada en GitHub**

#### 2.1 **Obtén la clave SSH pública**

Si ya tienes la clave generada, obtén el contenido de tu clave SSH pública (`id_rsa.pub`) con el siguiente comando:

```bash
cat ~/.ssh/id_rsa.pub
```

Copia el contenido de esta clave.

#### 2.2 **Revisa si tu clave está en GitHub**

Ve a [GitHub](https://github.com) e inicia sesión. Luego, sigue estos pasos:

1. En la parte superior derecha de GitHub, haz clic en tu foto de perfil, luego en **Settings**.
2. En el menú lateral, selecciona **SSH and GPG keys**.
3. Verifica si ves una clave SSH registrada en la lista.
   - Si no tienes una clave registrada, puedes agregar una nueva clave haciendo clic en **New SSH Key** y pegando el contenido de tu clave pública (`id_rsa.pub`).

### 3. **Prueba la conexión SSH con GitHub**

Una vez que hayas verificado que la clave SSH está registrada en GitHub, prueba la conexión desde tu terminal:

```bash
ssh -T git@github.com
```

Si todo está configurado correctamente, deberías ver un mensaje como:

```
Hi tu_usuario! You've successfully authenticated, but GitHub does not provide shell access.
```

Esto confirma que tu clave SSH está correctamente vinculada y que puedes usar SSH para interactuar con GitHub.

### 4. **Verifica la configuración SSH en Git**

También puedes verificar que Git está configurado para usar la autenticación SSH en lugar de HTTPS. Para esto, ve al directorio de tu repositorio local y ejecuta:

```bash
git remote -v
```

Si ves URLs que comienzan con `git@github.com:`, significa que Git está usando SSH. Si ves URLs que comienzan con `https://`, significa que Git está usando HTTPS.

Si necesitas cambiar de HTTPS a SSH, puedes hacerlo con el siguiente comando:

```bash
git remote set-url origin git@github.com:TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
```

### Resumen de pasos:

1. Verifica si tienes una clave SSH generada en `~/.ssh`.
2. Asegúrate de que tu clave SSH pública esté registrada en GitHub.
3. Prueba la conexión con GitHub usando `ssh -T git@github.com`.
4. Verifica que Git esté usando SSH con `git remote -v`.

Si sigues estos pasos, podrás asegurarte de que tu clave SSH está correctamente vinculada tanto en tu sistema como en GitHub.
