# Archivos y directorios de VMware

En VMware, las máquinas virtuales (VM) están definidas por varios archivos y directorios que contienen configuraciones, datos del disco, y otros aspectos necesarios para su funcionamiento. 

Las máquinas virtuales de VMware pueden componerse de dos directorios principales, o bien reunir en uno solo toda la información.

1. Directorio de configuración de la máquina: Basicamente contiene los settings e información sobre las instantaneas
2. Directo de almacenamiento de la imagen de disco duro virtual.

Todos los datos se pueden llegar a reunir en un solo directorio ya que VMware tiene una forma particular de nombrar los ficheros .vmdk que representan la unidad de disco virtual que equivale a un HDD/SSD en una máquina real.

En una maquina virtual determinada habrá bastante ficheros `.vmdk`, y atendiendo a su nombre podemos ver la finalidad para la que han sido creados. 
En mi caso la máquina ha sido nombrada como "Ubuntu 64-bit" por lo que está será la raiz común a todos los ficheros. 
Puesto que es una máquina que ha reservado 80GB en disco, el sistema no crea un único archivo de 80Gb sino que lo divide en varios. El principal se llama:

`Ubuntu 64-bit.vmdk`

Este fichero es muy pequeño ya que unicamente define como se compone el disco virtual completo de la máquina. Es decir da la información que apunta a todos los ficheros siguientes:

`Ubuntu 64-bit-f001.vmdk` hasta `Ubuntu 64-bit-f021.vmdk` 

todos ellos de prácticamente 4GB ~ 20 x 4 = 80GB

Estos ficheros representan el estado del disco virtual equivalente al HDD/SSD de la maquina en ese momento concreto.
Ademas duarante el uso de la MV se van a generar otros ficheros `.vmdk`

`Ubuntu 64-bit-000001-s001.vmdk` a `Ubuntu 64-bit-000001-s021.vmdk`

Donde el primer grupo de números `000001` hace referencia a la primera instantánea (snapshot)
Según se van creando nuevas instantaneas aparecerán más cantidad de ficheros, por ejemplo para la segunda snapshot:

`Ubuntu 64-bit-000002-s001.vmdk` a `Ubuntu 64-bit-000002-s021.vmdk`

Para el caso de está máquina el espacio necesario en disco en la maquina anfitriona (host), cuando tan solo se tienen 3 snapshot es de unos 100GB.
No obstante, para los backups es conveniente generar archivos comprimdos que suelen reducirse hasta el orden de los 10GB. 

Tras este inciso, pasamos a ver los principales archivos y directorios que componen una VM en VMware:

### 1. **Directorio de la máquina virtual:**
   - Cada máquina virtual tiene su propio directorio que contiene todos los archivos relacionados con ella.

### 2. **Archivos principales:**

   - **Archivo de configuración (`.vmx`):**
     - Contiene toda la configuración de la VM, como la memoria asignada, CPU, dispositivos de red, y más.
     - Ejemplo: `mi_maquina_virtual.vmx`.

   - **Archivo de disco virtual (`.vmdk`):**
     - Este es el archivo que contiene el disco duro virtual de la máquina. Puede estar dividido en varios archivos si se seleccionó la opción de dividir el disco en fragmentos.
     - Ejemplo: `mi_maquina_virtual.vmdk`.

   - **Archivo de memoria suspendida (`.vmss`):**
     - Se genera cuando una máquina virtual es suspendida. Contiene el estado de la memoria en el momento de la suspensión.
     - Ejemplo: `mi_maquina_virtual.vmss`.

   - **Archivo de snapshot (`.vmsn`):**
     - Se genera cuando se crea un snapshot (captura del estado de la máquina virtual). Contiene el estado de la memoria y el estado del sistema en ese momento.
     - Ejemplo: `mi_maquina_virtual.vmsn`.

   - **Archivo de logs (`.log`):**
     - Registra eventos y errores de la máquina virtual para fines de diagnóstico.
     - Ejemplo: `vmware.log`.

### 3. **Otros archivos importantes:**

   - **Archivo de descripción de discos (`.vmsd`):**
     - Contiene información sobre los snapshots de la VM. Se actualiza cada vez que se crea, elimina o modifica un snapshot.
     - Ejemplo: `mi_maquina_virtual.vmsd`.

   - **Archivo de swap de memoria (`.vswp`):**
     - Este archivo es utilizado para la memoria virtual de la VM cuando no hay suficiente memoria física disponible en el host.
     - Ejemplo: `mi_maquina_virtual.vswp`.

   - **Archivo de estado de BIOS (`.nvram`):**
     - Almacena la configuración del BIOS de la máquina virtual.
     - Ejemplo: `mi_maquina_virtual.nvram`.

   - **Archivos temporales (`.vmem`):**
     - Estos archivos almacenan datos de la memoria de la máquina virtual mientras está en ejecución. Son archivos temporales y se eliminan cuando la VM se apaga correctamente.
     - Ejemplo: `mi_maquina_virtual.vmem`.

### 4. **Snapshots:**
   Cuando creas un snapshot, VMware genera varios archivos adicionales relacionados con el estado de la memoria y los cambios en los discos virtuales.

Estas son las partes más relevantes de la estructura de una máquina virtual en VMware. Todos estos archivos deben estar presentes en su directorio correspondiente para que la máquina virtual funcione correctamente.
