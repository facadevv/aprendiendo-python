# Hola mundo, esto es un comentario
# nuestro hola mundo en python
print("hello python")

"""
este es un comentario en 
varia lineas sin poner #
en cada una
"""

#  type sirve consultar el tipo de dato
print(type("soy un dato str"))      # <class 'str'>    "string" = cadena de texto
print(type(5))                      # <class 'int'>    "integer" = numeros enteros
print(type(5.5))                    # <class 'float'>   decimales
print(type(True))                   # <class 'bool'>   "booleans"


#  variables 
name = "Ruben"

print("Hola soy", name)

# (len(name))   cuenta los caracteres impresos, al parecer solo texto por lo que pude probar

len(name)
num_let = len(name)

print("Este es el numero de letras en mi nombre:", num_let)

# Variables en una sola linea 
surname, alias, age = "Farias", "el triste", 27

print("mi nombre es", name, surname, "y mi apodo es", alias, "y tengo", age, "años")

len(surname)
nsurname =len(surname)
len(alias)
nalias = len(surname)

print("ah, y linea anterior son:",num_let+nsurname+nalias+20, "letras")

# Inputs
name_2 = input("¿cual es tu nombre? ")
age_2 = int(input("¿y cuantos años tienes? "))

if(age_2 > 27): print("orale", name_2, "eres mayor que yo")
if(age_2 < 27): print("tas morro ", name_2)
if(age_2 > 26): print("eea, empate jaja")
