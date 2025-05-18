
def hay_repetidos(numeros):
    vistos = set()
    for num in numeros:
        if num in vistos:
            return True
        vistos.add(num)
    return False

entrada = input("Ingresa números separados por espacios: ")

lista_numeros = list(map(int, entrada.split()))

if hay_repetidos(lista_numeros):
    print("¡Hay números repetidos en la lista!")
else:
    print("No hay números repetidos en la lista.")
