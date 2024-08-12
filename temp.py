import random
import time

def generar_temperatura():
    while True:
        temperatura = round(random.uniform(-10.0, 40.0), 2)
        print(f"Temperatura: {temperatura}°C")
        time.sleep(5)

if __name__ == "__main__":
    generar_temperatura()
