# And, or, not

# and : Cuando usamos el operador 'and' confirmamos que nuestras dos opciones son True, si alguna de los dos no lo es seran False

# Ejemplo:

2 > 1 and 2 < 3  # En este caso las dos afirmaciones son correctas por lo cual nos retornara un True.
# True + True = True

2 < 1 and 2 > 3  # en este caso una de las afirmaciones es False por lo cual nos retornara que la operacion es False
# False + True = False

gasolina = True
encendido = True

if gasolina and encendido:              # En este caso comprobamos que si las dos variables son True podemos encender el coche. 
    print("Puedes andar en el carro")
else: 
    print("No puedes andar")            # De lo contrario no podriamos.

# or : Cuando usamos el operador 'or' nos referimos a que si una de las afirmaciones es True, la comparacion lo sera, para que sea falso las dos afirmaciones tendrian que ser falsas

2 > 1 or 2 < 1 # En este caso una de las dos afirmaciones es correcta, asi que nos retorana un True
# True + False = True

2 < 1 and 2 > 3
# False + False = False

tareas = True
examen = False

if tareas or examen:
    print("Muy bien alcanzaste a pasar la materia!") # Como uno de los dos casos es True nos indicara que podemos pasar la materia.
else:
    print("Tristemente tienes que repetir") # Este es el hipotetico caso de que las dos afirmaciones sean False. 


# not : not es una negacion retornando el valor contrario a lo que diga el operador logico.

tiempo = False
dinero = True
amor = True

if not tiempo and (dinero or amor):
    print("Puedes hacer cualquier cosa")
else: 
    print("Necesitas ponerte a trabajar")






