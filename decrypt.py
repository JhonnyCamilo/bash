def rotr(x, k, bits=16):
    """Rotación a la derecha de x por k bits en un bloque de tamaño bits"""
    return (x >> k) | ((x << (bits - k)) & ((1 << bits) - 1))

def rotl(x, k, bits=16):
    """Rotación a la izquierda de x por k bits en un bloque de tamaño bits"""
    return ((x << k) & ((1 << bits) - 1)) | (x >> (bits - k))

def simon_round_inverse(L, R, K):
    """Realiza una ronda inversa del cifrado Simon"""
    S1 = rotl(L, 1)
    S8 = rotl(L, 8)
    S2 = rotl(L, 2)
    
    # Aplicación del AND entre S1 y S8 y luego XOR con S2
    F = (S1 & S8) ^ S2
    
    # Nueva parte izquierda y derecha
    new_R = L
    new_L = R ^ F ^ K
    
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

def simon_decrypt(ciphertext, key, rounds=32):
    """Descifra el texto cifrado usando el cifrado Simon"""
    # Dividir el texto cifrado en dos partes de 16 bits
    L = (ciphertext >> 16) & 0xffff
    R = ciphertext & 0xffff
    
    # Generar las subclaves en orden inverso
    subkeys = key_schedule(key, rounds)[::-1]
    
    # Ejecutar las rondas de descifrado en orden inverso
    for i in range(rounds):
        L, R = simon_round_inverse(L, R, subkeys[i])
    
    # Recombinar las dos partes
    plaintext = (L << 16) | R
    return plaintext

def leer_ciphertext():
    """Lee el texto cifrado desde el archivo y lo convierte a un entero"""
    with open('temperatura_cifrada.txt', 'r') as file:
        formatted_ciphertext = file.read().strip()
    
    # Reconvertir el texto formateado en un entero
    parts = formatted_ciphertext.split('_')
    hex_str = parts[2] + parts[3] + parts[0] + parts[1]
    return int(hex_str, 16)

def main():
    # Clave y número de rondas para el cifrado Simon
    key = 0x0123456789abcdef
    rounds = 32
    
    # Leer el texto cifrado desde el archivo
    ciphertext = leer_ciphertext()
    
    # Descifrar el dato de temperatura
    decrypted_value = simon_decrypt(ciphertext, key, rounds)
    
    # Convertir el valor descifrado de nuevo a temperatura
    temperatura = decrypted_value / 100.0
    
    print(f"Texto cifrado: {ciphertext:08x} -> Temperatura descifrada: {temperatura:.2f}°C")

if __name__ == "__main__":
    main()
