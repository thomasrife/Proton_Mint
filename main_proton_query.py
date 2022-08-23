from ntpath import join
from pydoc_data.topics import topics
from unittest import result
import requests
import pandas as pd
import json
from contract_events import dict_of_events

input_event = input("Event (Mint, Transfer, AproveForAll, SalePriceSet, UniverseSet): ")
input_from_block = input("From Block: ")
input_to_block = input("To Block: ")
input_address = input("Address: ")
input_page = input("Page: ")
input_offset = input("Offset: ")
input_apikey = input("ApiKey: ")

query_http = "https://api.etherscan.io/api?module=logs&action=getLogs"
query_from_block = f"&fromBlock={input_from_block}"
querty_to_block = f"&toBlock={input_to_block}"
query_address = f"&address={input_address}"
query_page = f"&page={input_page}"
query_offset = f"&offset={input_offset}"
query_apikey = f"&apikey={input_apikey}"

input_event_values = list(dict_of_events[input_event].__dict__.values())

def url_maker(event_topics):
    
    url_start = query_http + query_from_block + querty_to_block + query_address
    url_ends = query_page + query_offset + query_apikey
    
    counter = 0
    topics = []
    for topic in event_topics:
        if topic != '':
            topics.append(f"&topic{counter}={event_topics[counter]}")
            counter += 1
    url_topic = ''.join(topics)
    return url_start + url_topic + url_ends

url = url_maker(input_event_values)

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