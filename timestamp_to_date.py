from datetime import datetime
from time import time_ns
import pandas as pd

input_csv = input('Insert relative path to file: ')
event_name = input(("Event (Mint, Transfer, AproveForAll, SalePriceSet, UniverseSet): "))
mint_csv = pd.read_csv(input_csv)

timestamp = []
for time in mint_csv['timeStamp']:
    timestamp.append(datetime.fromtimestamp(int(time, 0)).strftime('%d-%m-%y'))

dates = []
for date in timestamp:
    print(date)
    dates.append(date)

col1 = 'dates_of_events'
result = pd.DataFrame({col1:dates})

file_name = f'results/dates_of_events_{event_name}.xlsx'
result.to_excel(file_name, index=False)
print(f'Se guardó el archivo {file_name}')



