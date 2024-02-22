# Ejercicio: Contar vocales

# Escribe una función llamada contar_vocales que tome una cadena de texto como entrada y devuelva un diccionario que contenga el recuento de cada vocal (a, e, i, o, u) en la cadena. Ignora las diferencias entre mayúsculas y minúsculas.

# Por ejemplo:

# print(contar_vocales("Hola mundo"))  # Debería imprimir: {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}
# print(contar_vocales("Python es genial"))  # Debería imprimir: {'a': 0, 'e': 1, 'i': 1, 'o': 1, 'u': 0}


def contar_vocales(string_value):
    string_value = string_value.lower()
    dict_vocales = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0
    }
    
    for char in string_value:
        if char in dict_vocales:
            dict_vocales[char] += 1
        
    return dict_vocales


print(contar_vocales("Hola mundo"))
# print(contar_vocales("Python es genial"))  # Debería imprimir: {'a': 0, 'e': 1, 'i': 1, 'o': 1, 'u': 0}
