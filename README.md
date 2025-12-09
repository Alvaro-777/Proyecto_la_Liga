# PROYECTO PROGRAMACIÓN ESTRUCTURADA Y MODULAR (LIGA)
Ejercicio de 7 funciones, realizado por Álvaro Colmenero y Alejandro Medel

Partiendo del fichero csv liga.csv con los resultados de las jornadas de liga 2015-2016, realizar un programa que muestre la tabla de clasificación al final de la liga, en el que debe aparecer el orden en que ha quedado cada equipo, los partidos ganados, los partidos empatados y los partidos perdidos, y por último los puntos conseguidos. Para realizar este programa vamos a construir varias funciones:

Alejandro Medel se encargara de:
- LeerPartidos(): Función que lee el fichero CSV y devuelve los datos del mismo en una lista de diccionarios.
- Equipos(datosliga): Función que recibe la lista de diccionarios con los datos de la liga y devuelve un conjunto con los equipos de la liga.
- QuienGana(resultado): Función que recibe un resultado y devuelve un 0 si es un empate, un 1 si gana el equipo de casa y -1 si gana el equipo visitante.
- Clasificacion(datos): Recibe la lista generada con la función anterior y la ordena según el número de puntos.

Álvaro Colmenero se encarga de:
- impClasificacion(liga): Recibe la lista de diccionarios generado a partir de la función anterior, genera los datos de la clasificación y los imprime por pantalla.
- InfoEquipos(datosliga,equipos): Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.
- Puntos(info): Función que recibe una lista con los partidos ganados, empatados y perdidos y devuelve los puntos obtenidos.
