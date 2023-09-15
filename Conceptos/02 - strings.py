nombre_curso = "Ultimate Python" ## Variable normal

variable_descriptiva = """
Ultimate python 

este curso contempla detalles que necesitas aprender para
encontrar un trabajo como programador
""" ## Esta variable tambien es interpretada como un comentario en nuestro codigo

print(len(nombre_curso)) # Nos cuenta la cantidad de caracteres que asignamos utilizando "len" abreviacion de Lenght en ingles que significa largo, Esta herramienta nos ayuda a contar cualquier tipo de dato en nuestro codigo.
    #output: 15
print(nombre_curso[0]) # Utilizando Variable[] podemos acceder al indice de nuestras variables
    # Output: U
print(nombre_curso[0:8]) # Tambien podemos fraccionar el contenido de nuestra variable asignando el indice donde queremos que empiece a recortar y la cantidad de items que deseamos recortar, en este caso empezamos desde el indice 0 y decimos que avance por 8 espacios.
    # Output: Ultimate
print(nombre_curso[8:]) # Cuando dejamos un espacio vacio python interpretara el espacio vacio por un valor por defecto, en este caso el indice maximo el string
    # Output: Python
print(nombre_curso[:8]) # o en el caso de que ea un espacio vacio al inicio lo tomara como 0 el valor por defecto
    # Output: Ultimate
print(nombre_curso[0:8:2]) # Tambien podemos hacer que fraccione indicandole un intervalo de espacios, haciendo que tome la informacion de la variable en saltando indices o dandole un orden especifico, En este caso se indico que saltara de 2 en 2
    # Output: Utmt 
print(nombre_curso[::-1])  # Por otro lado tambien podemos hacer que nuestro string sea escrito al revez de la siguiente manera