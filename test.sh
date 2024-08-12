#!/bin/bash

# Ruta a los archivos Python
archivo_generar_temperatura="generar_temperatura.py"
archivo_cifrado="simon_cifrado.py"

# Ejecutar el script de generación de temperatura en segundo plano
python3 "$archivo_generar_temperatura" &

# Guardar el PID del proceso de generación de temperatura
pid_generar_temperatura=$!

# Esperar unos segundos para asegurar que el archivo de temperatura se ha generado
sleep 5

# Ejecutar el script de cifrado
python3 "$archivo_cifrado"


