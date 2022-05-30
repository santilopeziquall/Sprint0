#!/bin/bash
STRING_FREE=`cat salida_free.txt`
Memoria_Total=$(echo $STRING_FREE | awk -v N=8 '{print $N}')
Memoria_EnUso=$(echo $STRING_FREE | awk -v N=9 '{print $N}')
Memoria_Libre=$(echo $STRING_FREE | awk -v N=10 '{print $N}')
Memoria_Compartida=$(echo $STRING_FREE | awk -v N=11 '{print $N}')
Memoria_BuffCache=$(echo $STRING_FREE | awk -v N=12 '{print $N}')
Memoria_Disponible=$(echo $STRING_FREE | awk -v N=13 '{print $N}')
JSON_FMT='{"Memoria_Total":"%s","Memoria_EnUso":"%s","Memoria_Libre":"%s","Memoria_Compartida":"%s","Memoria_BuffCache":"%s","Memoria_Disponible":"%s"}\n'
printf "$JSON_FMT" "$Memoria_Total" "$Memoria_EnUso" "$Memoria_Libre" "$Memoria_Compartida" "$Memoria_BuffCache" "$Memoria_Disponible"

