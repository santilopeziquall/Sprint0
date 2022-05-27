# Problemas que me fueron saliendo
#### WSL utiliza init en ves de systemd para los services
Solucion:
https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate


Nota: Esto rompe el interop de WSL con Windows. Para restaurarlo a la normalidad realizar un wsl --shutdown

### Instalacion de grafana
https://computingforgeeks.com/how-to-install-grafana-on-ubuntu-linux-2/

### Instalacion de Kapacitor

https://portal.influxdata.com/downloads/
 
Ir hasta la version 1.x open source y buscarlo ahi

Errores que tuve: Cuando quize arrancar el servicion de kapacitor me salio errores de permisos de kapacitor.log y kapacitor.db, lo solucione
cambiando sus permisos con chmod 666 en las carpetas que estaban

--- MUCHOS ERRORES DE PERMISOS -- 

https://docs.influxdata.com/kapacitor/v1.6/introduction/getting-started/#start-kapacitor