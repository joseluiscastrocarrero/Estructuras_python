# EJERCICIOS LISTAS

# EJERCICIOS manipulación

#1. Consiste en una defición de una lista con elementos de diferentes tipos y en mostrarlas por la pantalla,
#tanto entera como por elementos accediendo a la posición que ocupa dentro de la lista.

lista = ["Python","Guanentá",2022, "Libro",3]
print(lista)
print(lista[0])
print(lista[2])
#2. Consiste en el uso del operador + para realizar uniones de listas. Además, utilizar la función len para conocer el numero de elementos que componen la lista.
lista1 = ["camiseta", "pantalon","Zapatillas"]
lista2 = ["Abrigo","jersey","Sudadera","Calcetines"]
print("Número elementos lista1: ", len(lista1))
print("lista1: ", lista1)
print("Número elementos lista2: ", len(lista2))
print("lista1: ", lista2)
lista_Concatenada = lista1 + lista2
print("Número elementos lista_concatenada: ", len(lista_Concatenada))
print("lista_concatenada: ", lista_Concatenada)

#3. Añadir elelmentos a la lista de diferentes formas
lista = ["camiseta", "pantalon","Zapatillas"]
print(lista)
lista = lista + ["Abrigo"]
print(lista)
lista = lista + ["jersey","Sudadera"]
print(lista)
lista = lista + ["Calcetines"] + ["Bufanda"]
print(lista)

#4. Modificar elementos de una lista y borrar elementos de la misma
lista = ["camiseta", "pantalon","Zapatillas"]
print(lista)
lista[1] = "Cazadora"
print(lista)
del lista[0]
print(lista)

#5. Uso del operador * que perimite concatenar una lista con ella misma un número finito de veces.
lista = ["camiseta", "pantalon","Zapatillas"]
print(lista)
lista_resultante = lista * 3
print(lista_resultante)

#6. Creación de lista como elementos de lista y acceso a dichos elementos.
print("-------Ejercicio 6-------")
lista = ["Camiseta",["Calsetines","Cazadores"],"Zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])
#7. Extraer una porción de la lista een una lista nueva.
print("-------Ejercicio 7-------")
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2 = lista[:5]
print(lista2)
lista3 = lista[6:]
print(lista3)