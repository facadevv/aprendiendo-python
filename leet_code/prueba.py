def romano_a_decimal(numero_romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    while i < len(numero_romano):
        # Si este número es menor que el siguiente número
        if i + 1 < len(numero_romano) and valores[numero_romano[i]] < valores[numero_romano[i + 1]]:
            total += valores[numero_romano[i + 1]] - valores[numero_romano[i]]
            i += 2
            
        # En caso contrario, solo suma este número
        else:
            total += valores[numero_romano[i]]
            i += 1

    return total

def es_romano_valido(numero_romano):
    # Verifica si el número romano cumple con las reglas de los números romanos
    import re
    patron = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return re.search(patron, numero_romano) is not None

numero_romano = input("Ingresa un número romano: ").upper()
if es_romano_valido(numero_romano):
    print(romano_a_decimal(numero_romano))
else:
    print("El número romano ingresado no es válido.")
