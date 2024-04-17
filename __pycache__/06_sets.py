                                    #Sets

my_set=set()
my_other_set={}

print(type(my_other_set))           #* Inicialmente es un diccionario (cuando esta vacio, debido al tipado dinamico)
my_other_set={"ruben","farias",27}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("hello")           #* Permite agregar elementos
print(my_other_set)                 #* Un set no es una estructura ordenada
my_other_set.add("hello")           #* Un set no admite elementos repetidos

print("ruben" in my_other_set)      # in sirve para comprobar si exite cierto elemento en el set      
print("rubem" in my_other_set)      

my_other_set.remove("ruben")        # tambien se pueden elimiar elementos
print(my_other_set)

my_other_set.clear()                # se permite vaciarlo                   
print(len(my_other_set))                 

del my_other_set                    # y eliminar con del
#print(my_other_set)                NameError: name 'my_other_set' is not defined

my_set={"ruben","farias",27}
my_list=list(my_set)
print(my_list)
print(my_list[0])