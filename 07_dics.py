                    # Diccionarios

my_dict=dict()
my_other_dict={}

my_other_dict={"Nombre":"ruben","Apellido":"Farias","edad":27,1:"Python"}   #"Nombre":"ruben" es un item del diccionario

my_dict={                                                                   #otra forma de mostrarlo, mas visual
    "Nombre":"ruben",
    "Apellido":"Farias",
    "Edad":27,
    "Lenguajes":{"Python","Javascript","C#"},
    1:1.167
    }
print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])                                                    #de esta manera se accede a un valor asociado a una key

my_dict["Nombre"]="Pedro"                                                   #de esa manera se puede cambiar un valor asociado a una key
print(my_dict["Nombre"])

my_dict["Calle"]="C. Paseo del cantíl"
print(my_dict)

del my_dict["Calle"]                                                        #se elimina todo el item(key/value)
print(my_dict)

print(my_dict.keys())                                                       #muestra todas las keys del diccionario
print(my_dict.items())                                                      #muestra todos los itema
print(my_dict.values())                                                     #muestra todos los valores


