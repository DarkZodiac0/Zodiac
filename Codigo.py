

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar al usuario que ingrese un número
n = int(input("Ingrese un número para verificar si es primo: "))

# Verificar si el número es primo
if es_primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")