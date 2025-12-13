import csv

def leerPartidos() -> list[dict[str, str]]:
    """
    Función que lee el archivo liga.csv y lo devuelve como
    una lista de diccionarios
    
    :return: El contenido del archivo en una lista de diccionarios
    :rtype: list[dict]
    """
    with open('liga.csv', 'r', encoding="utf-8",) as fCSV:
        content = list(csv.DictReader(fCSV))
    fCSV.close()
    return content

def impClasificacion(liga: list[dict[str, str]]) -> None:
    """
    Genera la clasificación y la muestra por pantalla
    
    :param liga: Datos de la liga
    :type liga: list[dict[str, str]]
    """
    conj_equipos = equipos(liga)
    datos = infoEquipos(liga, conj_equipos)

    # ordenar por puntos (último elemento de la tupla)
    datos = clasificacion(datos)

    print(" Nº|     Equipo      | PG | PE | PP | Puntos")
    print("---------------------------------------------")

    posicion = 1
    for equipo, pg, pe, pp, pts in datos:
        print(f"{posicion:2} | {equipo:15} | {pg:2} | {pe:2} | {pp:2} | {pts:3}")
        posicion += 1

def equipos(datosliga: list[dict[str, str]]) -> set[str]:
    """
    Función que recibe la lista de diccionarios con los datos 
    de la liga y devuelve un conjunto con los equipos de la liga.
    
    :param datosliga: Le pasamos los datos extraidos del csv
    :type datosliga: list[dict[str, str]]
    :return: Retorna los equipos
    :rtype: set[str]
    """
    equipos = set()
    for partido in datosliga:
        equipos.add(partido["Team 1"])
        equipos.add(partido["Team 2"])
    return equipos

def infoEquipos(datosLiga: list[dict[str, str]], equipos: set[str]) -> list[tuple[str, int, int, int, int]]:
    """
    Recibe los datos de la liga y el conjunto de equipos.
    Devuelve una lista de tuplas con la informacion del equipo
    
    :param datosLiga: Lista de diccionarios con la informacion de la liga
    :type datosLiga: list[dict[str, str]]
    :param equipos: Conjunto de equipos que participan en la liga
    :type equipos: set[str]
    :return: Lista de tuplas de cada equipo:
    (equipo, ganados, empatados, perdidos, puntos)
    :rtype: list[tuple[str, int, int, int, int]]
    """
    info = list[tuple]()

    for equipo in equipos:
        ganados = 0
        empatados = 0
        perdidos = 0

        for partido in datosLiga:
            resultado = quienGana(partido["FT"])

            if partido["Team 1"] == equipo:
                if resultado == 1:
                    ganados += 1
                elif resultado == 0:
                    empatados += 1
                else:
                    perdidos += 1

            elif partido["Team 2"] == equipo:
                if resultado == -1:
                    ganados += 1
                elif resultado == 0:
                    empatados += 1
                else:
                    perdidos += 1

        pts = puntos([ganados, empatados, perdidos])
        info.append((equipo, ganados, empatados, perdidos, pts))

    return info

def quienGana(resultado: str) -> int:
    """
    Funcion que determina que equipo gana en base a un resultado (FT)
    
    :param resultado: Una cadena de caracteres con el resultado de un partido
    :type resultado: str
    :return: 1 si gana Team 1, -1 si gana Team 2 y 0 si empatan
    :rtype: int
    """
    separatorIndex = resultado.index('-')
    ptsCasa = int(resultado[:separatorIndex])
    ptsVist = int(resultado[separatorIndex:])
    
    if ptsCasa > ptsVist: 
        return 1
    if ptsCasa < ptsVist:
        return -1
    return 0

def puntos(info: list[int]) -> int:
    """
    Recibe una lista de cantidades de partidos agrupadas
    por resultados y devuelve los puntos
    
    :param info: Una lista con los partidos ganados, empatados
    y perdidos del equipo, en ese orden
    :type info: list[int]
    :return: La puntuacion final de un equipo en la liga:
    (3 x ganados) + empatados
    :rtype: int
    """
    if len(info) != 3:
        raise TypeError ("La funcion puntos solo acepta listas de 3 enteros")
    
    ganados = info[0]
    empatados = info[1]
    return ganados * 3 + empatados

def clasificacion(datos: list[tuple[str, int, int, int, int]]) -> list[tuple[str, int, int, int, int]]:
    """
    Funcion que ordena una lista de tuplas en base a los puntos
    en orden descendente
    
    :param datos: Lista de tuplas con los datos de los equipos
    :type datos: list[tuple[str, int, int, int, int]]
    :return: La lista de tuplas ordenada
    :rtype: list[tuple[str, int, int, int, int]]
    """
    return sorted(datos, key=lambda x: x[4], reverse=True) 

#---------------------------------------------

datosliga = leerPartidos()
impClasificacion(datosliga)


