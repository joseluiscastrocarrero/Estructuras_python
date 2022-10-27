# EJEMPLOS DE TUPLAS

#Tanto en las listas como en las tuplas, los elementos empiezan por la posición 0, no por la 1 como pareceria lo obvio. Tenlo en cuenta cuando utilices tuplas.
#En el siguiente ejercicio vamos a ver cómo definir una tupla y cómo acceder a sus elementos. El código fuente es el siguiente:
print("-------Ejercicio 1-------")
tupla = ('Casa', '2',345, 'Perro',99)
print("Elementos de la tupla: ", tupla)
print("Elemento de la posición 0: ", tupla[0])
print ("Elemento de la posición 1: ", tupla[1])
print("Elemento de la posición 2: ", tupla[2])
print("Elemento de la posición 3: ", tupla[3])
print("Elemento de la posición 4: ", tupla[4])

#Función count: cuenta el número de veces que aparece el elemento indicado como parámetro dentro de la tupla.
#Función index: devuelve la posición de la primera ocurrencia de izquierda a derecha en la tupla del elemento pasado como parámetro.

#Ahora vamos a realizar un ejercicio para aprender a utilizar ambas funciones de las tuplas. Y el codigo fuente es el siguiente:
print("-------Ejercicio 2-------")
tupla = ('Casa', '2',99,345, 'Perro',99) 
print("Elementos de la tupla: ", tupla)
print("Número de elementos 99: ", tupla.count (99))
print("Posición que ocupa el elemento Perro: ", tupla.index("Perro"))

#Las tuplas, al igual que las listas, permiten extraer posiciones de ellas en otra tupla nueva. La extracción se realiza utilizando la siguiente instrucción:
#Tupla[n:m]: la instrución extraer una nueva tupla que empezará en el indice n y terminará en el m-1. Tienes que tener en cuenta lo siguiente:

#no siempre tiene que ser menor que m.
#Si no se especifica el valor para n se supone que es 0.
#Si no se especifica el valor para m se supone que es el tamaño de la lista menos uno.
print("-------Ejercicio 3-------")
tupla = (1,2,3,4,5,6,7,8,9)
print(tupla)
print(tupla[4:9]) 
print(tupla[:3])
print(tupla[2:])

#Función "+": Dicha Funciónse llama len y devuelve un entero que indica el numero de elementos que la componen.
#Númeroelementos = Len(Tuplas):
print("-------Ejercicio 4-------")
tupla1 = (29, "Televisión", 8763)
tupla2 = (1,2,3, "Videojuego")
print("Número elementos de tupla1: ",len (tupla1))
print("Tuplal: ", tupla1)
print("Número elementos de tupla2: ", len(tupla2))
print("Tupla2: ", tupla2)
tuplaconcatenada = tupla1 + tupla2
print("Número elementos de tuplaconcatenada: ", len(tuplaconcatenada)) 
print("tuplaconcatenada: ", tuplaconcatenada)

#Función "*":Permite concatenar una tupla con ella misma un número finito de veces. Y lo utilizaremos el operador de la siguiente manera:
#TuplaResultante  = Tupla*NúmeroEntero
# La tupla resultante de la multiplicación será una tupla compuesta por tantas veces la tupla como valor tenga el número entero.
print("-------Ejercicio 5-------")
tupla = (1,2,3,4,5,6,7,8,9,0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)