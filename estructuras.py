# Ejercicio 1
numeros = [23, 65, 24, 4, 135]
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print(f"El número mayor es: {mayor}")
# Ejercicio 2
num = [1, 1, 1, 2, 2, 3, 3, 3, 3]
numero = int(input("Introduce un número: "))
contador = num.count(numero)
print(f"El número {numero} aparece {contador} veces en la lista.")
# Ejercicio 3
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2
print(f"Lista combinada: {lista_combinada}")
# Ejercicio 4
programacion = {'C++':'1', 'JavaScript':'2', 'Python':'3', 'Java':'4'}
index = input("Introduce un lenguaje: ")
print(programacion.get(index.title(), "El lenguaje no está."))
# Ejercicio 5
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"