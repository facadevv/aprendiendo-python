### Lists

my_list=list()                      #los dos tipos de constructores de listas
my_list=[27,35,62,52,30,30,17]      #si utilizamos solamente los parentesis se convierte en un tuple

print(my_list)
print(len(my_list))

my_other_list=[27,1.67, "ruben","farias"]

print(type(my_other_list))

#   para acceder a elemtos de una lista
#   con(-)comienza a contar desde el ultimo elemento -1 para el ultimo 
#   -2 para el penultimo etc. etc.

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))  #count devuelve el numero de ocurrencias de un valor

age,height,name,surname=my_other_list
print(name)

                                        ###OPERACIONES CON LISTAS###

print(my_list+my_other_list)

my_other_list.append("nuevo elemento")  #.append inserta un elemento nuevo al final de la lista
print(my_other_list)

my_other_list.insert(1,"green")         #.insert inserta un nuevo elemento pero al índice seleccionado (index,elemento)
print(my_other_list)                    #y recorre los elementos un indice a la derecha
my_other_list[1]="blue"                 #llamando a una lista seguida del indice(((list[index]=value))) declaramos un nuevo valor eliminando al que ocupaba ese indice
print(my_other_list)

my_other_list.remove("blue")           
print(my_other_list)                    #.remove elimina un elemento en especifico
my_list.remove(30)                      #pero elimina solo al primer elemento que coincida, no a todos
print(my_list)                          

my_list.pop()                           #.pop elimina el ultimo elemento por defecto pero ademas retorna el elemento eliminado
print(my_list)                          #(si se desea guardar posteriormete dicho elemento hay declarar una variable y asignarla al pop)

del my_list[2]                          #del elimina el elemento  sin guardarlo (por indice)
print(my_list)

my_new_list=my_list.copy()              #.copy copia los elementos de una lista

my_list.clear()                         #.clear elimina los elmenentos de una lista

print(my_list)                          #los que se hizo fue declarar my_new_list igualandola a los elementos copiados de my_list con my_list.copy()
print(my_new_list)                      #por ello, aunque despues los elementos de my_list fueron eliminados con my_list.clear se guardaron en my_new_list quedando la misma con los elementos y my_list quedando vacia




