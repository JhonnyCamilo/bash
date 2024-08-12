def rotr(x, k, bits=16):
    """Rotación a la derecha de x por k bits en un bloque de tamaño bits"""
    return (x >> k) | ((x << (bits - k)) & ((1 << bits) - 1))

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

        # Alternar c en la ronda 9 y volver a alternar en la ronda 10
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
    
    # Convertir las subclaves a formato hexadecimal y mostrarlas
    subkeys_hex = [f'{subkey:04x}' for subkey in subkeys]
    return subkeys_hex

# Ejemplo de clave y generación de subclaves
key = 0x0123456789abcdef
rounds = 32
subkeys = key_schedule(key, rounds)
for i in range(len(subkeys)):
    print(i,subkeys[i])
