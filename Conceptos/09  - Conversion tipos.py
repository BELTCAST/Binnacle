# Conversion de tipos

# Dentro de python hay varias funciones nativas que nos ayudan a convertir datos, por ejemplo:

# int(): Convierte en entero todo numero contenido dentro de su parentesis

# str(): Convierte en string todo tipo de dato que se almacene dentro de su parentesis

# float(): Como su nombre lo indica convierte el numero o cadena de caracteres en un numero de punto flotante
valor = 3.14  # Esto es un número de punto flotante
texto = "42.0" # Esto es un string
numero_decimal = float(valor)  # Convierte 'valor' a un número de punto flotante
numero_desde_cadena = float(texto)  # Convierte 'texto' a un número de punto flotante
print(numero_decimal)  # Imprime 3.14
print(numero_desde_cadena)  # Imprime 42.0

# bool() : Puede transformar cualquier dato en un booleano, este evalua los datos si son True o False
    # Datos Falsy: Espacios vacios " ", el none , Retornara False
print(bool(""))
print(bool(0))
print(bool(None))
    # Datos Truly: Contienen numeros enteros, strings o datos contrarios a Falsy
print(bool("Hola!"))
print(bool(1234))

print(float(4.76786786))