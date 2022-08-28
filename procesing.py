import hashlib
from time import perf_counter

def encript_first_elemnt(languages):
    hashlib.sha1(list(languages.values())[0].encode()).hexdigest()

def dict_generate(data):
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