import hashlib
from time import perf_counter

def encript_first_elemnt(languages):
    """
    Función encargada de encriptar el primer elemento de la lista de lenguajes.
    Args:
        - languages: Dict | Lista de lenguajes del País
    Returns:
        - : Str | cadena encriptada
    """
    return hashlib.sha1(list(languages.values())[0].encode()).hexdigest()

def dict_generate(data):
    """
    Función encargada de procesar el JSON obtenido para generar un diccionario con la información relevante
    Args:
        - data: JSON| información sin procesar
    Returns:
        -  : dict | información procesada
    """
    dicc = {'region':[], 'city_name':[], 'language':[], 'time':[]}
    data_json = data.json()

    for i in data_json:
        start = perf_counter()
        dicc['city_name'].append(i['name']['common'])
        dicc['region'].append(i['region'])
        if('languages'in i):
            dicc['language'].append(encript_first_elemnt(i['languages']))
        else:
            dicc['language'].append("")
        end = perf_counter()
        dicc['time'].append((end - start) * 1000)

    return dicc