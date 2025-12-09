def equipos(datosliga) -> set:

    """
    Recibe la lista de diccionarios generado a partir de la 
    función anterior, genera los datos de la clasificación y los imprime por pantalla.
    
    :param datosliga: Le pasamos los datos extraidos del csv
    :return: Retorna los equipos
    :rtype: set
    """

    equipos = set()
    for partido in datosliga:
        equipos.add(partido["Team 1"])
        equipos.add(partido["Team 2"])
    return equipos


