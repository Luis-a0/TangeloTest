import requests
import pandas as pd
from procesing import dict_generate

URL = "https://restcountries.com/v3.1/all"

if __name__ == '__main__':
    data = requests.get(URL)

    if data.status_code == 200:
        dicc = dict_generate(data)
    
    df = pd.DataFrame(dicc)
    df.to_json('data.json')

    v_min, v_mean, v_max, v_total = df['time'].min(), df['time'].mean(), df['time'].max(),df['time'].sum()

    print(f"Valor minimo: {v_min}, valor promedio: {v_mean}, valor maximo: {v_max}, valor total: {v_total}")