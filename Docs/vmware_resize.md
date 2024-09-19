# Aumentar el tamaño del disco virtual en Ubuntu corriendo en VMWare
https://www.youtube.com/watch?v=brR0G7Fg3i0

## Verificar el uso del disco (2 formas diferentes)
````bash
df -h
````
````bash
lsblk
````

En mi caso el disco sda se encuentra dividido en tres particiones siendo sda3 la que nos preocupa.

Apagar la maquina virtual y cambiar tamaño.

Al arrancar de nuevo usar:
````bash
sudo cfdisk
````
Esto abre la herramienta que nos permitirá asignar elespacio libre a sda3. Para ello, seleccionar con los cursores sd3 y la opción Resize.
Confirmar el incremento y finalmente seleccionar la opcion Write y Quit para salir

El proceso todavía no está terminado. 
Si se consulta de nuevo con
````bash
lsblk
````
se confirma el incremento de tamaño pero al usar
````bash
df -h
````
vemos que todavia no está aplicado donde nos interesa, que es en sda3. Para hacerlo faltará lo siguiente:
````bash
sudo resize2fs /dev/sda3
````

Tras esto se comprueba que todo es correcto con 
````bash
df -h
````
