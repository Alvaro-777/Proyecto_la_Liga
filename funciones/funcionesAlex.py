import csv

def leerPartidos() -> list:
    with open('liga.csv', 'r', encoding="utf-8",) as fCSV:
        content = list(csv.reader(fCSV))
    fCSV.close()
    return content