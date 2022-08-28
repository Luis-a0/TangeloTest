import requests
import pandas as pd
import hashlib
import time

if __name__ == '__main__':
    URL = "https://restcountries.com/v3.1/all"
    data = requests.get(URL)
    dicc = {'region':[], 'city_name':[], 'language':[], 'time':[]}

    if data.status_code == 200:
        data_json = data.json()

        for i in data_json:
            start = time.perf_counter()
            dicc['city_name'].append(i['name']['common'])
            dicc['region'].append(i['region'])
            if('languages'in i):
                dicc['language'].append(hashlib.sha1(list(i['languages'].values())[0].encode()).hexdigest())
            else:
                dicc['language'].append("")
            end = time.perf_counter()
            dicc['time'].append((end - start) * 1000)

    df = pd.DataFrame(dicc)
    df.to_json('data.json')

    print(f"""Valor minimo: {df['time'].min()}, 
valor promedio: {df['time'].mean()},
valor maximo: {df['time'].max()},
valor total: {df['time'].sum()}""")