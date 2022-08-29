import requests
import pandas as pd

from procesing import dict_generate
import db

URL = "https://restcountries.com/v3.1/all"

if __name__ == '__main__':
    data = requests.get(URL)

    if data.status_code == 200:
        dicc = dict_generate(data)
    
    df = pd.DataFrame(dicc)
    df.to_json('data.json')

    list_values = [df['time'].min(), df['time'].mean(), df['time'].max(),df['time'].sum()]
    v_min, v_mean, v_max, v_total = list_values

    db.create_record(list_values)

    print(f"""Valor minimo: {v_min}ms,
valor promedio: {v_mean}ms,
valor maximo: {v_max}ms,
valor total: {v_total}ms""")