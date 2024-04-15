                                                                        ### Classes ###

class Person:                                                           ## Aqui def no esta definiendo una funcion, #*def __init__(self, name, ...) es un construtor de clase
    def __init__(self, name, surname, alias="sin alias"):               #* un lugar donde podemos establecer ciertos valores asociados a la clase (persona en este caso)            # Tambien se puede asignar valores por defecto###
        self.full_name=f"{name} {surname} ({alias})"                    #* Aqui lo que se crear es la propiedad full_name almacenada en la clase Person                              ### y se puede colocar parentesis sin problema              


    def walk (self):                                                    #* Para definir funciones dentro de una clase en necesario pasarle el self al parametro de la funcion                           
        print(f"{self.full_name} está caminando")                       #* y asi poder acceder a todo lo guardado dentro de self 


my_person=Person("ruben","farias")                                      # Aqui se definen desde fuera de la clases los valores name y surname(que #* tambien se pueden definir desde dentro como se hizo con full_name)
print(my_person.full_name)                                              # Aqui lo que se hace es acceder a la propiedad full_name desde la variable my_person llamando con .full_name a dicha propiedad

my_person.walk()                                                        # y asi creas tu propia funcion para tu propia clase

my_other_person= Person("ruben", "farias","el triste")                  # se define otro objeto "Persona" utilizando la misma clase y se le otorga la propiedad de .full_name
print(my_other_person.full_name)                                        
my_other_person.full_name=("Hector de León (El loco de los perros)")    # se modifica la propiedad full_name de la nueva Persona
print(my_other_person.full_name)

