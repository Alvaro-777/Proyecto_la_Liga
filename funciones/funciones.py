import csv

def leerPartidos() -> list[dict]:
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

def impClasificacion(liga: list[dict]) -> None:
    """
    Genera la clasificación y la muestra por pantalla
    
    :param liga: Datos de la liga
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

def equipos(datosliga) -> set:
    """
    Función que recibe la lista de diccionarios con los datos 
    de la liga y devuelve un conjunto con los equipos de la liga.
    
    :param datosliga: Le pasamos los datos extraidos del csv
    :return: Retorna los equipos
    :rtype: set
    """
    equipos = set()
    for partido in datosliga:
        equipos.add(partido["Team 1"])
        equipos.add(partido["Team 2"])
    return equipos

def infoEquipos(datosLiga: list[dict], equipos: set) -> list[tuple]:
    """
    Recibe los datos de la liga y el conjunto de equipos.
    Devuelve una lista de tuplas:
    (equipo, ganados, empatados, perdidos, puntos)
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
    separatorIndex = resultado.index('-')
    ptsCasa = int(resultado[:separatorIndex])
    ptsVist = int(resultado[separatorIndex:])
    
    if ptsCasa > ptsVist: 
        return 1
    if ptsCasa < ptsVist:
        return -1
    return 0

def puntos(info: list) -> int:
    """
    Recibe una lista [ganados, empatados, perdidos]
    y devuelve los puntos (3-1-0)
    
    :param info: Descripción
    :type info: list
    :return: Descripción
    :rtype: int
    """
    ganados = info[0]
    empatados = info[1]
    return ganados * 3 + empatados

def clasificacion(datos: list[tuple]) -> list:
    return sorted(datos, key=lambda x: x[4], reverse=True) 

#---------------------------------------------

datosliga = leerPartidos()
#print(datosliga[0]['FT'])
impClasificacion(datosliga)


