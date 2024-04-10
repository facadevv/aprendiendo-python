                                                ###  Strings #formateo

name = "ruben"
surname = "farias"
age = 27

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))   #para concatenar especificando el tipo de dato (%s para strin(texto)) (%d para int (numero entero))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")          #para concatenar colocando directamente el objeto 

                                            #Desempaquetado de caracteres

language="Python"
a, b, c, d, e, f = language
#(0)(1)(2)(3)(4)(5)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f) 

                                                    #Division

language_slice = language[0:5] #[0:5] Toma en cuenta desde los carcateres desde el 0 hasta el 4, sin contar al 5
print(language_slice)

language_slice = language[0:] #[0:] Toma en cuenta desde el 0 hasta el final
print(language_slice)

language_slice = language[-2] #[-2] Toma en cuenta el segundo comenzando desde el final
print(language_slice)

                                                    #Reverse

reversed_language = language[::-1] #[::-1]Ordena los caracteres en reversa 
print(reversed_language)