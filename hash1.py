def contar_palabras(texto):
    palabras = texto.lower().split()

    frecuencia = {}
    
    for palabra in palabras:
    
        palabra = palabra.strip(".,!?:;\"'")

        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

texto_usuario = input("Ingresa una frase o párrafo: ")

resultado = contar_palabras(texto_usuario)

print("\nFrecuencia de palabras:")
for palabra, conteo in resultado.items():
    print(f"{palabra}: {conteo}")

