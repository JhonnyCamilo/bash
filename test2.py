import random
import time

def rotr(x, k, bits=16):
    """Rotación a la derecha de x por k bits en un bloque de tamaño bits"""
    return (x >> k) | ((x << (bits - k)) & ((1 << bits) - 1))

def rotl(x, k, bits=16):
    """Rotación a la izquierda de x por k bits en un bloque de tamaño bits"""
    return ((x << k) & ((1 << bits) - 1)) | (x >> (bits - k))

def simon_round(L, R, K):
    """Realiza una ronda del cifrado Simon"""
    S1 = rotl(R, 1)
    S8 = rotl(R, 8)
    S2 = rotl(R, 2)
    
    # Aplicación del AND entre S1 y S8 y luego XOR con S2
    F = (S1 & S8) ^ S2
    
    # Nueva parte izquierda y derecha
    new_L = R
    new_R = L ^ F ^ K
    
    return new_L, new_R

def key_schedule(key, rounds=32):
    """Generación de subclaves para las rondas"""
    subkeys = [0] * rounds
    subkeys[0] = key & 0xffff
    subkeys[1] = (key >> 16) & 0xffff
    subkeys[2] = (key >> 32) & 0xffff
    subkeys[3] = (key >> 48) & 0xffff

    # Valor inicial de c
    c = 0xfffd

    for i in range(4, rounds):
        temp = rotr(subkeys[i - 1], 3)
        temp1 = temp ^ subkeys[i - 3]
        temp2 = rotr(temp1, 1)
        temp3 = temp1 ^ subkeys[i - 4]
        temp4 = temp3 ^ temp2

        # Alternar c según las reglas dadas
        if i == 9:
            c = 0xfffc
        elif i == 10:
            c = 0xfffd
        elif i == 11:
            c = 0xfffc
        elif i == 14:
            c = 0xfffd
        elif i == 15:
            c = 0xfffc
        elif i == 17:
            c = 0xfffd
        elif i == 18:
            c = 0xfffc
        elif i == 19:
            c = 0xfffd
        elif i == 20:
            c = 0xfffc
        elif i == 21:
            c = 0xfffd
        elif i == 23:
            c = 0xfffc
        elif i == 27:
            c = 0xfffd
        elif i == 30:
            c = 0xfffc

        subkeys[i] = temp4 ^ c
    
    return subkeys

def simon_encrypt(plaintext, key, rounds=32):
    """Cifra el texto plano usando el cifrado Simon"""
    # Dividir el texto plano en dos partes de 16 bits
    L = (plaintext >> 16) & 0xffff
    R = plaintext & 0xffff
    
    # Generar las subclaves según el esquema dado
    subkeys = key_schedule(key, rounds)
    
    # Ejecutar las rondas de cifrado
    for i in range(rounds):
        L, R = simon_round(L, R, subkeys[i])
    
    # Recombinar las dos partes
    ciphertext = (L << 16) | R
    return ciphertext

def format_ciphertext(ciphertext):
    """Formatea el texto cifrado en bloques de dos caracteres separados por guiones bajos"""
    hex_str = f'{ciphertext:08x}'  # Convierte a hexadecimal de 8 dígitos
    formatted = f'{hex_str[4:6]}_{hex_str[6:]}_{hex_str[:2]}_{hex_str[2:4]}'
    return formatted

def generar_temperatura():
    """Genera un dato de temperatura aleatorio con 2 decimales"""
    return round(random.uniform(-10.0, 40.0), 2)

def main():
    # Clave y número de rondas para el cifrado Simon
    key = 0x0123456789abcdef
    rounds = 32
    
    while True:
        # Generar un dato de temperatura
        temperatura = generar_temperatura()
        
        # Convertir la temperatura a un entero (por ejemplo, multiplicado por 100)
        plaintext = int(temperatura )
        
        # Cifrar el dato de temperatura
        ciphertext = simon_encrypt(plaintext, key, rounds)
        
        # Formatear el texto cifrado
        formatted_ciphertext = format_ciphertext(ciphertext)
        
        # Guardar el texto cifrado en un archivo
        with open('temperatura_cifrada.txt', 'w') as file:
            file.write(formatted_ciphertext)
        
        print(f"Temperatura: {temperatura}°C -> Cifrado: {formatted_ciphertext}")
        
        # Esperar 5 segundos antes de generar y cifrar un nuevo dato
        time.sleep(5)

if __name__ == "__main__":
    main()
