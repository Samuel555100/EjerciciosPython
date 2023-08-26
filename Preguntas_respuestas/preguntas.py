import random

preguntas_respuestas = [

    ("¿Cuál es la capital de Argentina?", "Buenos Aires"),

    ("¿En qué año llegó el hombre a la luna?", "1969"),

    ("¿Cuál es el río más largo del mundo?", "Amazonas"),

    ("¿Quién escribió la Odisea?", "Homero"),

    ("¿Cuál es el océano más grande del mundo?", "Pacífico")

]

random.shuffle(preguntas_respuestas)

puntuacion = 0

for pregunta, respuesta in preguntas_respuestas:

    print(pregunta)

    usuario_respuesta = input().lower()

    if usuario_respuesta == respuesta.lower():

        print("¡Respuesta correcta!")

        puntuacion += 1

    else:

        print(f"Respuesta incorrecta. La respuesta correcta es {respuesta}.")

print(f"Tu puntuación final es {puntuacion} de {len(preguntas_respuestas)} preguntas.")