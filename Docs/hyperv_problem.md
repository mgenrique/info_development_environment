Tras tener todo el sistema funcionando, se produjo un fallo en la virtualización que necesita hacer VMware
Posiblemente esto sucedió posteriormente a la instalación de Docker en la maquina Windows que ejecuta VMware Workstation.

Para solucionarlo he seguido los pasos del tutorial del siguiente video
https://www.youtube.com/watch?v=6f1Qckg2Zx0&t=226s

Procedures followed:

1. Disable Hyper-V via the GUI and restart the system.

2. Use systeminfo and msinfo32 to check the status of Hyper-V.

3. Deactivate the hypervisor launch type.

Command: bcdedit /set hypervisorlaunchtype off”

4. Using PowerCLI, remove all Hyper-V features.

Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All


En el simbolo de sistema ejecutado como administrador ejecutar:
````bash
bcdedit /set hypervisorlaunchtype off
````

En PowerShell ejecutado como administrador ejecutar:
````bash
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All
````
Finalmente aunque no lo indique como requisito se debe reiniciar.
