palabra = "paralelepípedo"
eliminar = "aeío"
sinvocales = palabra

for character in eliminar:
    sinvocales = sinvocales.replace(character, "")
print(sinvocales)

consonantes = ""
for i in range(len(palabra)):
    if palabra[i] not in eliminar:
        consonantes += palabra[i]
        print(f"la letra {palabra[i]} se encuentra en la posicion {i}")

