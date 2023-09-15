animal = "chanchito feliz"

print(animal.upper())  # Metodo para combertir un string en MAYUSCULA
print(animal.lower())  # Metodo para convertir un string en minuscula
print(animal.capitalize()) # Metodo para convertir la primera letra en MAYUSCULA
print(animal.title()) # Metodo que convierte en MAYUSCULA todas las iniciales dentro del String
print(animal.strip()) # Metodo Que se encarga de borrar todos los espacios del inicio y el final.
print(animal.lstrip()) # Metodo Que se encarga de borrar todos los espacios de la izquierda del string
print(animal.rstrip()) # Metodo Que se encarga de borrar todos los espacios de la derecha del string
print(animal.find("ch")) # Metodo que nos ayuda a buscar dentro de una cadena de caracteres una entrada especifica y nos retornara su indice, de no encontrarlo retornara un numero negativo.
print(animal.replace("ch", "j")) # Metodo que nos ayuda a buscar un string y remplazarlo con otro.
print("ch" in animal) # Metodo que a diferencia de "find" nos retornara un boolean en vez de un integer, con este podemos buscar un indice y nos retornara True or False.


# Se pueden combinar metodos? 

print(animal.strip().capitalize()) # Se llama encadenacion de metodos y podemos unirlos para poder sacar un 