                                        #* Exceptions *#

number_one=5
number_two=1
#number_two="1"                                         

# try: - except:
                                                                # Un strin y un int no se pueden operar
try:                                                            # try: como la palabra lo dice intenta ejecutar un codigo
    print(number_one+number_two)                
    print("ejecucion esperada")
    print("-----------------------------------------------") 

except:                                                         # except: ejecuta lo que se programó ahí si hay un error con try:
    print("Se ha produciod un error")
    print("-----------------------------------------------")    # no se detiene el programa 

# try: except: else:

try:
    print(number_one+number_two)                
    print("ejecucion esperada")
except:                                                 
    print("Se ha produciod un error")
    print("-----------------------------------------------")
else:                                                           #* else: se ejecuta solo cuando try: funcionó correctamente
    print("La ejecucion continua correctamente")
    print("-----------------------------------------------")

# try: - except: - else: - finally:

try:
    print(number_one+number_two)                
    print("ejecucion exitosa")
except:                                                 
    print("Se ha producido un error")
else:                                                   
    print("La ejecucion continúa correctamente")
finally:                                                        # finally: es opcional y se ejecuta siempre
    print("La ejecucion continúa ejemplo del finally")
    print("-----------------------------------------------")

# Captura de excepciones por tipo
number_two="1"

try:                                                            
    print(number_one+number_two)                
    print("ejecucion esperada") 

except TypeError:                                               #* Colocando el tipo de error esperado despues de except se ejecuta esa excepcion solo si ese tipo de error es el causante                                      
    print(":c Se ha producido un error del tipo: TypeError")
    print("-----------------------------------------------")
except:                                                         #* Se debe colocar otro except: adicional para evitar que el programa se detenga por cualquier otro error inesperado
    print("Error no encontrado")

# Captura de la informacion del error ocurrido

try:
    print(number_one+number_two)
    print("No se ha producido un error")
except ValueError as error:                                     # *y con la palabra clave as e inmediatamente declarando una variable (error ... sería logico) se guarda en la misma la informacion del error
    print(":c Se ha producido un error del tipo: TypeError")    # para despues hacer con esa informacion lo que se crea conveniente
    print(error)                                                #* colocando Exception en lugar del tipo de error esperado es como poner solo el except sin más pero esta vez controlando y guardando la informacion de cualquier 
except Exception as error:                                      #* tipo de error y permitiendo a su vez guardar la info en la variable
    print("no se pudo ejecutar debido a este error:",error)
    print("-----------------------------------------------")
    
