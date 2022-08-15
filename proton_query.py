from unittest import result
import requests
import pandas as pd
import json
from contract_events import transfer, mint, aprove_for_all, sale_price_set, universe_set

input_event = input("Event (Mint, Transfer, AproveForAll, SalePriceSet, UniverseSet): ")
input_from_block = input("From Block: ")
input_to_block = input("To Block: ")
input_address = input("Address: ")
input_page = input("Page: ")
input_offset = input("Offset: ")
input_apikey = input("ApiKey: ")

dict_of_events = {'Transfer': transfer, 'Mint': mint, 'AproveForAll': aprove_for_all, 'SalePriceSet': sale_price_set, 'UniverseSet': universe_set}

def url_maker(inputEvent, fromBlock, toBlock, address, page, offset, apiKey):
    if dict_of_events[inputEvent].topic_1 != '':
        url_query_1 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={dict_of_events[inputEvent].topic_0}&topic0_1_opr=and&topic1={dict_of_events[inputEvent].topic_1}&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_1
    else:
        url_query_2 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={dict_of_events[inputEvent].topic_0}&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_2

url = url_maker(input_event,
input_from_block, 
input_to_block, 
input_address,  
input_page, 
input_offset, 
input_apikey)

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata = []

for x in myjson['result']:
    ourdata.append(x)

json_file_name = f"results/{input_event}_fromBlock_{input_from_block}_toBlock_{input_to_block}.json"

out_file = open(json_file_name, "w") 
    
json.dump(ourdata, out_file, indent = 4) 
    
out_file.close()

csv_file_name = f"results/{input_event}_fromBlock_{input_from_block}_toBlocl_{input_to_block}.csv"

pdObj = pd.read_json(json_file_name)
pdObj.to_csv(csv_file_name, index=False)

print('done')