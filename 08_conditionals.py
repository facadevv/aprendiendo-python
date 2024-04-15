                    #Condicionales

my_condition=False
if my_condition:    #Es lo mismo que ----> if my_condition == True: 
    print("se ejecuta la condicion del if")

my_condition=5*5

if my_condition==10:                                                        #if pide que se cumpla una condicion e inmediatamente
    print("Es igual a 10")                                                  #desencadena las acciones especificadas 

if my_condition>10 and my_condition<20:                                     #and añade una condicion mas a la verfificacion
    print("Es mayor que 10 y menor que 20")
elif my_condition==25:                                                      #elif se verifica solo si if y and no se complen
    print("Es igual a 25")
else:                                                                       #y si ninguna se cumple se ejecuta else:
    print("Es menor o igual que 10 o mayor que 20 o distinto de 25")        #esta linea está dentro del scope



print("La ejecucion continua")                                              #esta linea está fuera del scope                                             


                                                                            #*toda linea tabulada despues de una condicion se ejecuta si se cumple la misma
                                                                            #*para sacar un linea del escope es necesario borrar el tabulador (pegar la linea a la izquierda)

my_string=""                                                               
if my_string:                                                               #*si un string esta vacio"", un if lo toma como False
    print("Mi cadena de texto está vacia #incorrecta")                                  #y no se ejecuta ninguna accion
if not my_string:                                                           #para que se cumpla la condicion de un string vacio
    print("mi cadena de texto está vacia #correcta")                                  #*se debe usar --->if not<--- (negativo x negativo = positivo)


