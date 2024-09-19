# DEV CONTAINERS

Dentro de VS Code, se hará uso de la extensión Dev Containers, que permitirá el desarrollo de aplicaciones que corran en contenedores de Docker.

En Ubuntu y Visual Studio Code, los datos de los Dev Containers generalmente se almacenan en las siguientes rutas:

Archivos de configuración del contenedor:
`/ruta/al/proyecto/.devcontainer/`

Imágenes de Docker:
`/var/lib/docker`

Volúmenes de Docker (si se usan volúmenes para persistir datos entre sesiones):
`/var/lib/docker/volumes`
