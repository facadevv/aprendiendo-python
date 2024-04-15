                                        #Functions/Funciones

def my_function ():                                                         #*definir funciones no ES mas que CREAR TUS PROPIAS OPERACIONES para trabajar con variables
    print("Esto es una funcion")

my_function()                                                               #una funcion ejecuta el codigo programado solo llamandola sin volver a reescribir codigo
my_function()


def sum_two_values (firsts_v, second_v):                                    #*Los valores que se le pasen dentro del parentesis son interpretados como una tupla                                  
    print(firsts_v + second_v)

sum_two_values(5,7)
sum_two_values(21655,355444)
sum_two_values("5","7")                                                     #hay que tener cuidado al ingresar datos a una funcion ya que puede dar error o no funcionar como se espera
sum_two_values(1.4,5.2)

def sum_two_values_with_return (firsts_v, second_v):                        #*el return regresa un valor al terminar la funcion
    my_sum=(firsts_v + second_v)
    return my_sum

result = sum_two_values_with_return(10,2)                                   #*y ese valor regresado se puede guardar en una variable 
print(result)                                                               #para se utilizado posteriormente como ejemple en un print o lo que sea

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("ruben", "farias")

def print_name_with_default_value (name, surname, alias="sin alias"):       #*Asignando un valor a una variable definida dentro del parametro de una funcion-->variable=algo<--  
    print(f"{name} {surname} {alias}")                                      #*ocurre que al llamar la funcion si no se le proporciona dicho valor toma el valor asignado por defecto en el parametro

print_name_with_default_value("ruben", "farias")                                
print_name_with_default_value("ruben", "farias", "el triste")

def print_upper_texts(*texts):                                              #*Funcion con parametros arbirtrarios -->anteponiendo el * en los parametros de entrada-->def "nombre de la funcion" (*parametro):<--
    for element in texts:                                                   #*se puede trabajar con un numero indefinido de parametros
        print(element.upper())                                              #Ejemplo del loop for para cambiar de minusculas a mayusculas cuantas entradas se tengan


print_upper_texts("hola","que tal","¿como estas?")

def funcion_sin_parametro():                                                #y tambien se pueden definir funciones sin parametro
    nombre=input("¿como te llamas?")
    print("hola",nombre)

funcion_sin_parametro()