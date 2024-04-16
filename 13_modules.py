                                            #* Modules *#

import my_module                                                    # Para importar un modulo se usa import seguido del nombre del fichero a importar
                                                                    # y se importan todas las funciones que el mismo incluya 
my_module.sum(12,12,13)
my_module.printValue("Hola Python!")
print("----------------------------------------------")

                                                                    # Tambien se puede importar de la siguiente forma 
from my_module import sum, printValue                               # Pero sirve para las funciones declaradas unicamente

printValue("Otra forma de importar")
sum(1,2,3)
print("----------------------------------------------")

import math                                                         #* Python tiene muchos modulos preinstalados que podemos importar para su uso

print(math.pow(2,8))
print(math.pi)
from math import pi as pi_value
print(pi_value)
