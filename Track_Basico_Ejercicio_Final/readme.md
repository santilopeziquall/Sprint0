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

### Instalacion de influx db client

No viene influxdb con el cliente cuando se instala InfluxDB normalmente

Solucion:

```bash
sudo apt update
sudo apt install influxdb-client
```

### Usar los datos cargados de ansible con Grafana

Los datos que ansible carga se cargan como String pero para visualizarlos necesitamos que sean Numeric, asi que usamos una transformacion para convertir el fieldtype

https://grafana.com/docs/grafana/next/panels/transform-data/transformation-functions/



### Nota extra:

Revisar de tener dentro del venv de airflow todos las dependencias:

-Ansible 

-jmespath

-InfluxDB

Voy a generar un requirements.txt por si las dudas