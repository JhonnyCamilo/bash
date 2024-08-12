#!/bin/bash

# Ruta a los archivos Python
archivo_generar_temperatura="generar_temperatura.py"
archivo_cifrado="simon_cifrado.py"

# Ejecutar el script de generación de temperatura en segundo plano
python3 "$archivo_generar_temperatura" &

# Guardar el PID del proceso de generación de temperatura
pid_generar_temperatura=$!

# Bucle infinito para ejecutar el cifrado cada 5 segundos
while true; do
    # Ejecutar el script de cifrado
    python3 "$archivo_cifrado"

    # Esperar 5 segundos antes de la próxima ejecución
    sleep 5
done
