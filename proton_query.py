from unittest import result
import requests
import pandas as pd
import json

Event = input("Event: ")
FromBlock = input("From Block: ")
ToBlock = input("To Block: ")
Address = input("Address: ")
Topic = input("Topic: ")
Topic_1 = input("Topic 1: ")
Page = input("Page: ")
Offset = input("Offset: ")
ApiKey = input("ApiKey: ")

def url_maker(fromBlock, toBlock, address, topic, page, offset, apiKey):
    if Topic_1 != "":
        url_query_1 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={topic}&topic0_1_opr=and&topic1={Topic_1}&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_1
    else:
        url_query_2 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={topic}&topic0_1_opr=and&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_2

url = url_maker(FromBlock, ToBlock, Address, Topic, Page, Offset, ApiKey)

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata = []

for x in myjson['result']:
    ourdata.append(x)

json_file_name = f"{Event}_fromBlock_{FromBlock}_toBlocl_{ToBlock}.json"

out_file = open(json_file_name, "w") 
    
json.dump(ourdata, out_file, indent = 4) 
    
out_file.close()

csv_file_name = f"{Event}_fromBlock_{FromBlock}_toBlocl_{ToBlock}.csv"

pdObj = pd.read_json(json_file_name)
pdObj.to_csv(csv_file_name, index=False)

print('done')