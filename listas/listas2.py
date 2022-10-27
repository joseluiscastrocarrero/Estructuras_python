# EJERCICIOS LISTAS

# Métodos propios

lista = [45,32,3,78]
print("lista original: ", lista)
# Función append: añada un elemento a la lista
lista.append(995)
lista.append(7)
print("Lista después de usar append: ", lista)
# Función sort: ordena la lista
lista.sort()
print("lista ordenada: ", lista)
# Función reverse:inverse el orden de la lista
lista.reverse()
print("lista al revés: ", lista)
#Función  extend: Añade los elementos de una lista a la lista.
lista_extend = [1,5,87,45]
lista.extend(lista_extend)
print("lista después de extend: ", lista)
# FUnción count: Cuenta el número de veces que aparece el elemento indicado como parámetro de la lista.
print("Número de elementos 45: ", lista.count(45))
#Función insert: Añade el elemento pasado como parámetro a la lista en la posicion indicada también por parámetro.
lista.insert(4,111)
print("Lista depués de insert: ", lista)
#Funcion remove: Elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado como parametro
lista.remove(45)
print("Lista después de remove: ", lista)
#FUnción index:Devuelve la posicion de la primera ocurrencia a la derecha en la lista, del elemento pasado como parametro
print("posición del elemento 111: ", lista.index(111))
#Funcion pop: Elimina el ultimo elemento de la  lista y lo devuelve como resultado de la operacion. 
lista.pop()
print("List despues de pop: ", lista)
#Funcion clear: elimina todos los elementos de la lista.
lista.clear()
print("lista depsues de clear: ", lista)