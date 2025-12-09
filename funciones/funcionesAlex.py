import csv, funcionesAlvaro as fAvl

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

