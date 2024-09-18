
# Configuración de Docker Desktop y Visual Studio Code en Ubuntu

Este documento describe los pasos necesarios para configurar un entorno de desarrollo en Ubuntu, basado en Docker Desktop y Visual Studio Code, para desarrollar contenedores Docker.
La instalación se realiza sobre una maquina virtual que trabaja en VMWare Workstation 16 Pro, en la que se ha instalado el sistema operativo a partir de la imagen
ubuntu-24.04.1-desktop-amd64.iso

Los ajustes utilizados en VMWare se muestran a continuación:
![Ajustes 1](./images/VMware%20settings%2001.jpg)

Es importante para trabajar con Docker marcar la opción Virtualize Intel VT-x/EPT or AMD-V/RVI. Esto nos permitirá usar KVM virtualization support en Ubuntu

![Ajustes 2](./images/VMware%20settings%2002.jpg)
![Ajustes 3](./images/VMware%20settings%2003.jpg)

No se recomienda instalar las VMWare tools que proporciona VMware Workstation. Ubuntu utiliza las open-vm-tools y dan menos problemas

![VMware_tools](./images/VMware_tools.jpg)

Instalar open-vm-tools en Ubuntu
Asegúrate de tener open-vm-tools instalado en tu máquina virtual Ubuntu. Puedes hacerlo ejecutando los siguientes comandos en la terminal de Ubuntu:
```bash
sudo apt update
sudo apt install open-vm-tools open-vm-tools-desktop
```

## 1. Actualizar el sistema

Primero, asegúrate de que tu sistema esté actualizado:

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Instalar soporte para virtualización KVM

```bash
sudo apt update
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```
Para permitir que tu usuario normal gestione las máquinas virtuales, añade tu usuario al grupo libvirt:

````bash
sudo adduser $(whoami) libvirt
````
Comprueba que KVM está funcionando correctamente
````bash
sudo kvm-ok
````
Asegúrate de que los servicios de libvirt estén en ejecución y habilitados al inicio:
````bash
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
````
Para verificar quien es el propietario del servicio KVM 
````bash
ls -al /dev/kvm
````
Para añadir el usuario actual al grupo de usaurios con permiso para usar el servicio KVM 
````bash
sudo usermod -aG kvm $USER
````

## 2. Instalar dependencias necesarias

Docker Desktop requiere algunas dependencias adicionales que debes instalar:

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common linux-modules-extra-$(uname -r)
```

## 3. Instalar Docker Desktop

Sigue los siguientes pasos para instalar Docker Desktop en Ubuntu:

### 3.1 Descargar Docker Desktop para Linux:

Ve al sitio oficial de Docker y descarga la versión más reciente de Docker Desktop para Linux:

[Docker Desktop para Linux](https://www.docker.com/products/docker-desktop)

Alternativamente, puedes descargarlo usando `curl` en la terminal (ajusta el enlace según la versión más reciente):

```bash
curl -LO https://desktop.docker.com/linux/main/amd64/docker-desktop-<VERSION>-amd64.deb
```

### 3.2 Instalar Docker Desktop:

Una vez descargado el archivo `.deb`, instálalo con:

```bash
sudo dpkg -i docker-desktop-<VERSION>-amd64.deb
```

Si hay dependencias faltantes, puedes corregirlas con:

```bash
sudo apt --fix-broken install
```

### 3.3 Configurar Docker Desktop para ejecutarse como root:

Después de la instalación, es posible que necesites iniciar Docker Desktop con permisos de root:

```bash
sudo systemctl start docker
sudo docker run hello-world
```

### 3.4 Añadir tu usuario al grupo `docker` (opcional):

Para evitar usar `sudo` en cada comando de Docker, puedes añadir tu usuario al grupo `docker`:

```bash
sudo usermod -aG docker $USER
```

Luego cierra sesión y vuelve a entrar para aplicar los cambios.

## 4. Instalar Visual Studio Code

### 4.1 Instalar el repositorio de Microsoft para VS Code:

```bash
sudo apt install wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
```

### 4.2 Instalar Visual Studio Code:

```bash
sudo apt update
sudo apt install code
```

## 5. Configurar Visual Studio Code para Docker

### 5.1 Instalar la extensión de Docker:

Abre Visual Studio Code y busca la extensión **Docker** en el marketplace. También puedes instalarla desde la terminal con:

```bash
code --install-extension ms-azuretools.vscode-docker
```

### 5.2 Instalar la extensión de WSL (opcional):

Si planeas usar Docker con **WSL2** (Windows Subsystem for Linux), también deberías instalar la extensión **Remote - WSL**:

```bash
code --install-extension ms-vscode-remote.remote-wsl
```

## 6. Verificar la integración de Docker con Visual Studio Code

1. Abre Visual Studio Code.
2. En el panel lateral izquierdo, haz clic en el ícono de Docker (una ballena).
3. Deberías poder ver los contenedores, imágenes y redes de Docker en ejecución.
4. Crea un archivo `Dockerfile` en un proyecto y empieza a desarrollar tu contenedor.

## 7. Usar Docker Compose (opcional)

Si trabajas con múltiples contenedores, puedes usar Docker Compose. Instálalo con:

```bash
sudo apt install docker-compose
```

En **VS Code**, asegúrate de que la extensión de Docker también soporte la configuración de `docker-compose.yml`.

## 8. Probar la instalación

Crea un contenedor de prueba desde **VS Code**:

1. Abre un proyecto en VS Code.
2. Crea un archivo `Dockerfile`:

```Dockerfile
FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD ["npm", "start"]
```

3. Ejecuta el contenedor con los comandos de Docker integrados en el editor o desde la terminal.

Con estos pasos, tendrás un entorno de desarrollo completo para trabajar con contenedores Docker desde Ubuntu, usando Docker Desktop y Visual Studio Code.
