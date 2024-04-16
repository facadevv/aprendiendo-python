                                        #* loops (bucles, ciclos) *#

# While

my_condition=0
while my_condition<10:                                                  #* while es como un if pero se repite indefinidamente hasta que la condicion ya no se cumpla
    print(my_condition)
    my_condition += 2                                                   # con +=2 se le suma dos a my_condition en cada paso del loop
else:                                                                   # else se ejecuta si la condicion inicial no se cumple
    print(10)

while my_condition<20:                                                  
    my_condition+=1                                                     #* con +=1 se le suma uno a my_condition en cada paso del loop
    if my_condition ==15:                                               #* se pueden agregar condiciones intermedias en el while
        print("Mi condicion es igual a 15 y se detiene la ejecucion")
        break                                                           #* break sirve para detener el loop completo en el momento que se cumple una condicion intermedia-->if<--

    else:                                                               
        print(my_condition)

# For                                                                   #* for solo se repite dependiendo de el numero de elemntos con los que vaya a iterar
#                                                                       una vez finalizada la ultima iteracion se termina el loop
my_list=[27,24,62,52,30,30,17]

for element in my_list:                                                 # Con el for se declarara una variable element pero la misma
    print(element)                                                      # puede llamarse de cualquier forma, es solo para el print

my_dict={"Nombre":"ruben","Apellido":"Farias","edad":27,1:"Python"}

for key in my_dict:                                                     # En caso de un diccionario por defecto te devuelve la key
    print(key)

for value in my_dict.values():                                          # para obtener los valores de cada key se debe usar la operacion
    print(value)                                                        # .values()
else:
    print("El bucle ha finalizado")                                     # tambien se puede usar el else:

